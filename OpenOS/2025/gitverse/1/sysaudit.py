#!/usr/bin/env python3

from __future__ import annotations
from datetime import datetime
from git import Git, Repo, GitCommandError
from pathlib import Path
import argparse
import fnmatch
import logging
import pyinotify
import sys
import tempfile
import time

DEFAULT_LOG_LEVEL = logging.INFO


def dprint(*args, **kwargs):
    pass


import threading
from typing import List

class BatchProcessor:
    def __init__(self, callback, squash_period: float):
        self.callback = callback
        self.squash_period = squash_period
        self.message_queue: List[str] = []
        self.timer: threading.Timer | None = None
        self.lock = threading.Lock()  # To ensure thread safety

    def batch(self, message: str):
        with self.lock:
            self.message_queue.append(message)
            if not self.timer:
                self.timer = threading.Timer(self.squash_period, self._commit_and_reset)
                self.timer.start()

    def _commit_and_reset(self):
        with self.lock:
            queue = self.message_queue
            self.message_queue = []
            self.timer = None
        self.callback(queue)


class GitHelper:
    def __init__(self, path: str):
        self.repo = self._create_repository(path)
        self._repo_path = Path(path)

    def _create_repository(self, path: str):
        repo_path = Path(path).resolve()

        if not repo_path.exists():
            print(f"Creating directory: {repo_path}", file=sys.stderr)
            repo_path.mkdir(parents=True, exist_ok=True)

        # Check if it's already a git repo
        if not (repo_path / ".git").exists():
            print(f"Initializing new Git repository at: {repo_path}", file=sys.stderr)
            repo = Repo.init(repo_path)
            print("Repository initialized.", file=sys.stderr)
        else:
            print(f"Repository already exists at: {repo_path}", file=sys.stderr)
            repo = Repo(repo_path)

        # Set config for GPG signing
        # This ensures git uses GPG signing by default
        repo.config_writer().set_value("commit", "gpgsign", "true").release()

        return repo

    def commit(self, message, dry_run=False):
        if isinstance(message, list):
            msg = "\n".join(message)
        else:
            msg = str(message)

        if dry_run:
            print(
                f"git -C {self.repo_path()} commit -m '{message}' -S", file=sys.stderr
            )
            return

        try:
            # commit using temp file to prevent "Argument list too long" error
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".msg", delete=False
            ) as f:
                f.write(msg)
                temp_file_path = f.name
            self.repo.git.commit("-F", temp_file_path, gpg_sign=True, allow_empty=True)
        except GitCommandError as e:
            print(f"Failed to create commit: {e}", file=sys.stderr)
        else:
            Path(temp_file_path).unlink()

    def track(self, file: str, dry_run=False):
        if dry_run:
            print(f"git -C {self.repo_path()} add {file}", file=sys.stderr)
            return

        try:
            self.repo.git.add(file)
        except Exception as e:
            print(f"Failed to add {file} to git: {e}", file=sys.stderr)

    def message_series(self, begin, end):
        commits = self.repo.iter_commits(f"{begin}^..{end}", reverse=False)

        messages = []
        for commit in commits:
            messages.append(commit.message.strip())

        return messages

    def checkout_file(self, filename: str, to_commit: str, dry_run=False):
        if dry_run:
            print(
                f"git -C {self.repo_path()} checkout {filename} {to_commit}",
                file=sys.stderr,
            )
            return

        self.repo.git.checkout(to_commit, filename)

    def repo_path(self) -> Path:
        return self._repo_path


class FileAuditWatcher(pyinotify.ProcessEvent):
    class Record:
        def __init__(
            self, timestamp: str, path: str, operation: str, pid: str, tracked: bool
        ):
            self.timestamp = timestamp
            self.path = path
            self.operation = operation
            self.pid = pid
            self.tracked = tracked

        def __eq__(self, other: Record):
            if self.tracked or other.tracked:
                return False
            return (
                self.path == other.path
                and self.operation == other.operation
                and self.pid == other.pid
            )

    def __init__(
        self,
        watch_paths: list[Path],
        ignore_patterns: list[str],
        keep_patterns: list[str],
        track_paths: list[Path],
        log_output: str,
        squash_period: int,
        git_helper: GitHelper,
    ):
        self.watch_paths = [Path(p).resolve() for p in watch_paths]
        self.ignore_patterns = ignore_patterns
        self.keep_patterns = keep_patterns
        self.track_paths = track_paths
        self.log_output = log_output
        self.logger = self._setup_logger()
        self.squash_period = squash_period
        self.git_helper = git_helper

        self.batch_processor = BatchProcessor(
            self.git_helper.commit, self.squash_period
        )

        for track in self.track_paths:
            self._stage_external_file(Path(track))
        body = "\n - ".join([x.name for x in self.track_paths])
        timestamp = datetime.now().isoformat()
        self.git_helper.commit(f"[{timestamp}]: Started tracking files:\n - {body}")

    def _setup_logger(self) -> logging.Logger:
        logger = logging.getLogger("os-audit")
        logger.setLevel(DEFAULT_LOG_LEVEL)

        if self.log_output == "stdout":
            handler = logging.StreamHandler(sys.stdout)
        else:
            handler = logging.FileHandler(self.log_output, mode="a")

        logger.addHandler(handler)

        return logger

    def _stage_external_file(self, file_path: Path):
        # Construct destination path
        new_filename = str(file_path.absolute()).replace("/", "%")
        dest_file = self.git_helper.repo_path() / new_filename

        # Copy file to destination
        try:
            dest_file.write_bytes(file_path.read_bytes())
        except Exception as e:
            print(f"Failed to copy {file_path} to {dest_file}: {e}", file=sys.stderr)
        else:
            self.git_helper.track(new_filename)

    def _is_tracked(self, filepath: Path) -> bool:
        tracked = filepath in self.track_paths
        dprint("tracked" if tracked else "not tracked", filepath.name)
        return tracked

    def _is_ignored(self, filepath: Path) -> bool:
        rel = filepath.name

        for pattern in self.keep_patterns:
            if self._matches_pattern(rel, pattern):
                dprint("whitelisted", rel)
                # file whitelistet
                return False

        for pattern in self.ignore_patterns:
            if self._matches_pattern(rel, pattern):
                dprint("ignored", rel)
                # file ignored
                return True

        dprint("accepted", rel)
        return False

    def _matches_pattern(self, path: str, pattern: str) -> bool:
        return fnmatch.fnmatch(path, pattern)

    def _get_pid(self, event) -> str:
        # if pyinotify event has pid - simply return it
        try:
            return str(event.pid)
        except AttributeError:
            pass

        return "unknown process"

    def _parse_event(self, event) -> Record | None:
        path = Path(event.pathname).resolve()
        op = event.maskname
        if "IN_CREATE" in op:
            operation = "created"
        elif "IN_DELETE" in op:
            operation = "deleted"
        elif "IN_MOVED_TO" in op or "IN_MODIFY" in op:
            operation = "modified"
        elif "IN_ATTRIB" in op:
            perm = path.stat().st_mode & 0o777
            operation = f"changed attributes to {perm:03o}"
        else:
            operation = "unknown"

        tracked = False
        if self._is_tracked(path):
            self._stage_external_file(path)
            tracked = True
        elif self._is_ignored(path):
            return None

        timestamp = datetime.now().isoformat()
        pid = self._get_pid(event)

        return self.Record(
            timestamp=timestamp,
            path=str(path),
            operation=operation,
            pid=pid,
            tracked=tracked,
        )

    def _format_record(self, record: Record):
        tracked = "tracked" if record.tracked else ""
        return '[{}]: {} file "{}" {} by {}'.format(
            record.timestamp, tracked, record.path, record.operation, record.pid
        )

    def process_IN_CREATE(self, event):
        self._log_event(event)

    def process_IN_DELETE(self, event):
        self._log_event(event)

    def process_IN_MOVED_TO(self, event):
        self._log_event(event)

    def process_IN_MODIFY(self, event):
        self._log_event(event)

    def process_IN_ATTRIB(self, event):
        self._log_event(event)

    def _log_event(self, event):
        record = self._parse_event(event)
        if not record:
            return

        fmt = self._format_record(record)

        # log record to logger
        self.logger.info(fmt)

        # log event to repository

        self.batch_processor.batch(fmt)

    def process_default(self, event):
        # Ignore other events
        pass


def parse_args():
    parser = argparse.ArgumentParser(
        description="Infrastructure monitoring and management CLI tool.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
        required=True,
    )

    # monitor command
    monitor_parser = subparsers.add_parser(
        "monitor",
        help="Monitor infrastructure changes and state.",
    )
    monitor_parser.add_argument(
        "--watch",
        action="append",
        required=True,
        help="Directory to watch (can be used multiple times)",
    )
    monitor_parser.add_argument(
        "--ignore",
        action="append",
        default=[],
        help='File pattern to ignore (e.g., "*.tmp")',
    )
    monitor_parser.add_argument(
        "--keep",
        action="append",
        default=[],
        help="Whitelist file pattern to keep despite ignore rules",
    )
    monitor_parser.add_argument(
        "--track",
        action="append",
        default=[],
        help="Files to track full history with ability to roll back",
    )
    monitor_parser.add_argument(
        "--repo",
        required=True,
        help="Path of repository to store audition reports",
    )
    monitor_parser.add_argument(
        "--squash-period",
        type=int,
        default=5,
        help="Period (in seconds) to squash reports in to batches. Default: 5",
    )
    monitor_parser.add_argument(
        "--log",
        default="stdout",
        help='Log output file or "stdout". Default: stdout',
    )

    # snapshot command
    snapshot_parser = subparsers.add_parser(
        "snapshot",
        help="Create a snapshot of the current infrastructure state.",
    )
    snapshot_parser.add_argument(
        "--message",
        required=True,
        help="Message describing the snapshot.",
    )
    snapshot_parser.add_argument(
        "--repo",
        required=True,
        help="Path to the repository to snapshot.",
    )

    # drift-check command
    drift_check_parser = subparsers.add_parser(
        "drift-check",
        help="Check for configuration drift against a baseline.",
    )
    drift_check_parser.add_argument(
        "--baseline",
        required=True,
        help="Baseline commit SHA to compare against.",
    )
    drift_check_parser.add_argument(
        "--repo",
        required=True,
        help="Path to the repository to check for drift.",
    )

    # rollback command
    rollback_parser = subparsers.add_parser(
        "rollback", help="Roll back changes of tracked file."
    )
    rollback_parser.add_argument(
        "--to-commit",
        required=True,
        help="Commit SHA to roll back to.",
    )
    rollback_parser.add_argument(
        "--path",
        action="append",
        required=True,
        help="Paths to roll back (at least one required).",
    )
    rollback_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run without making changes.",
    )
    rollback_parser.add_argument(
        "--repo",
        required=True,
        help="Path to the repository where file tracked.",
    )

    return parser.parse_args()


def run_monitor(
    watch: list[str],
    ignore: list[str],
    keep: list[str],
    track: list[str],
    repo: str,
    squash_period: int,
    log: str,
):
    def validate_paths(paths: list[str], name: str, dir_only: bool, file_only: bool):
        for path in paths:
            p = Path(path)
            if not p.exists():
                print(f"Error: {name} path does not exist: {path}", file=sys.stderr)
                sys.exit(1)
            if dir_only and not p.is_dir():
                print(f"Error: {name} path is not a directory: {path}", file=sys.stderr)
                sys.exit(1)
            if file_only and p.is_dir():
                print(f"Error: {name} path is a directory: {path}", file=sys.stderr)
                sys.exit(1)

    validate_paths(watch, "Watch", True, False)
    validate_paths(track, "Track", False, True)

    # create watcher
    wm = pyinotify.WatchManager()

    # add watches
    mask = (
        pyinotify.IN_CREATE
        | pyinotify.IN_DELETE
        | pyinotify.IN_MOVED_TO
        | pyinotify.IN_MODIFY
        | pyinotify.IN_ATTRIB
    )
    for path in watch:
        wm.add_watch(path, mask, rec=True, auto_add=True)
    for path in track:
        wm.add_watch(path, mask)

    # initialize audit system
    watcher = FileAuditWatcher(
        watch_paths=[Path(p).resolve() for p in watch],
        ignore_patterns=ignore,
        keep_patterns=keep,
        track_paths=[Path(p).resolve() for p in track],
        log_output=log,
        squash_period=squash_period,
        git_helper=GitHelper(repo),
    )

    # start monitoring
    notifier = pyinotify.Notifier(wm, watcher)
    print("OS Audit System started. Press Ctrl+C to stop.")

    try:
        while True:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nShutting down...")
        notifier.stop()
        sys.exit(0)


def run_snapshot(message: str, repo: str):
    gh = GitHelper(repo)
    timestamp = datetime.now().isoformat()
    gh.commit(f"[{timestamp}]: {message}")


def run_drift_check(baseline: str, repo: str):
    gh = GitHelper(repo)
    print("\n".join(gh.message_series(baseline, "HEAD")))


def run_roll_back(to_commit: str, files: list[str], dry_run: bool, repo_path: str):
    repo = GitHelper(repo_path)

    for file_str in files:

        # Construct tracked file path
        file = Path(file_str).absolute().resolve()
        tracked_filename = str(file.absolute()).replace("/", "%")

        # Checkout file to requested commit state
        repo.checkout_file(tracked_filename, to_commit, dry_run)

        # Roll back original file from repository contents
        src_path = repo.repo_path() / tracked_filename
        if dry_run:
            print(f"cp {src_path} {file}", file=sys.stderr)
        else:
            try:
                file.write_bytes(src_path.read_bytes())
            except Exception as e:
                print(f"Failed to copy {src_path} to {file}: {e}", file=sys.stderr)
                continue

        # Make rollback commit (only if roll back was successful)
        timestamp = datetime.now().isoformat()
        repo.track(tracked_filename, dry_run)
        repo.commit(f"[{timestamp}]: Roll back {file.name} to {to_commit}", dry_run)


def main():
    args = parse_args()

    if args.command == "monitor":
        run_monitor(
            watch=args.watch,
            ignore=args.ignore,
            keep=args.keep,
            track=args.track,
            repo=args.repo,
            squash_period=args.squash_period,
            log=args.log,
        )
    elif args.command == "snapshot":
        run_snapshot(args.message, args.repo)
    elif args.command == "drift-check":
        run_drift_check(args.baseline, args.repo)
    elif args.command == "rollback":
        run_roll_back(args.to_commit, args.path, args.dry_run, args.repo)
    elif args.command == "metric-report":
        run_metric_report(args.repro)
    else:
        assert False


if __name__ == "__main__":
    main()
