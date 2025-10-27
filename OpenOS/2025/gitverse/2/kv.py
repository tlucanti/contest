from pathlib import Path
from git import Repo, Commit, GitCommandError
import argparse
import sys
from datetime import datetime

FILE_CONTENTS_IN_COMMIT_MESSAGE = False
REDUCED_TIMESTAMPS = False


def dprint(*args, **kwargs):
    pass


class KVStorage:

    def __init__(self):
        self.repo = Repo(".")

    @staticmethod
    def create_repo():
        if not Path(".git").exists():
            Repo.init(Path("."))
            print(f"Repository initialized at {Path('.').absolute()}")
            return True
        else:
            print(f"Repository already initialized")
            return False

    def init(self):
        self._commit("Initial commit", allow_empty=True)

    def set(self, key: str, value: str):
        self._write_file(key, value)
        self._add_file_to_index(key)
        if FILE_CONTENTS_IN_COMMIT_MESSAGE:
            self._commit(f"set {key} {value}")
        else:
            self._commit(f"set {key}")

    def get(self, key: str, commit: str | None) -> str | None:
        if commit is None:
            file_path = Path(key)
            if not file_path.exists():
                return None

            with open(file_path, "r") as f:
                return f.read()
        else:
            try:
                commit_obj = self.repo.commit(commit)
                blob = commit_obj.tree[key]
                return blob.data_stream.read().decode("utf-8")
            except Exception:
                return None

    def delete(self, key: str) -> bool:
        file_path = Path(key)
        if not file_path.exists():
            return False

        file_path.unlink()
        self._add_all_to_index()
        self._commit(f"delete {key}")
        return True

    def node_add(self, name: str, repo: str):
        self.repo.create_remote(name, repo)

    def node_delete(self, name: str):
        if name in self.repo.remotes:
            self.repo.delete_remote(name)
        else:
            print(f"Remote '{name}' does not exist.")

    def sync(self, name: str):
        if name not in self.repo.remotes:
            print(f"Remote '{name}' does not exist.")
            return

        self.repo.git.fetch(name, "master")
        self._switch("remote", force=True)
        self._reset(f"{name}/master")
        self._switch("master")

        self._merge_branches_histories("master", "remote", "tmp")
        self._switch("master")

        self._reset("tmp")
        self._del_branch("remote")
        self._del_branch("tmp")

        self.repo.git.push(name, "master", "--force")
        # self._del_branch("tmp")

    def sync_all(self):
        for remote in self.repo.remotes:
            self.sync(remote.name)

    def list_keys(self, dir: str):
        def print_tree(path: Path, prefix=""):
            if not path.exists():
                print(f"Error: {path} does not exist.")
                return
            if not path.is_dir():
                print(f"Error: {path} is not a directory.")
                return

            items = sorted([x for x in path.iterdir() if not x.name.startswith(".")])
            for i, item in enumerate(items):
                print(f"{prefix}- {item.name}" + ":" * item.is_dir())
                if item.is_dir():
                    print_tree(item, prefix + "   ")

        print_tree(Path(dir))

    def history(self, key: str):
        commits = list(self.repo.iter_commits(paths=key))
        if not commits:
            print(f"Key {key} does not exist.")
            return

        for commit in commits:
            sha = commit.hexsha
            message = commit.message.strip().splitlines()[0]
            print(f"{sha}: {message}")

    def _commit(self, message: str, allow_empty=False):
        timestamp = int(datetime.now().timestamp() * 1e6)
        if REDUCED_TIMESTAMPS:
            timestamp = timestamp // 10000 % 10000
        msg = f"{message}\n\n{timestamp}"
        self.repo.git.commit(message=msg, allow_empty=allow_empty)

    def _write_file(self, key: str, value: str):
        file_path = Path(key)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(value)

    def _add_file_to_index(self, key: str):
        self.repo.index.add([key])

    def _add_all_to_index(self):
        self.repo.git.add("--all")

    def _get_lca(self, b1: str, b2: str) -> Commit | None:
        lca = self.repo.merge_base(b1, b2)
        return lca[0] if lca else None

    def _get_commits_since(
        self, start_commit: Commit | None, branch: str
    ) -> list[Commit]:
        if not start_commit:
            return list(self.repo.iter_commits(f"{branch}"))[::-1]
        else:
            return list(self.repo.iter_commits(f"{start_commit}..{branch}"))[::-1]

    def _switch(self, branch: str, force=False):
        if force:
            self.repo.git.switch("-C", branch)
        else:
            self.repo.git.switch(branch)

    def _reset(self, commit: Commit):
        self.repo.git.reset("--hard", commit)

    def _get_commit_timestamp(self, commit: Commit) -> int:
        return int(commit.message.strip().split("\n")[-1])

    def _extract_commit_key(self, commit: Commit) -> str:
        key = list(commit.stats.files.keys())[0]
        dprint(f"extracted {commit.message.strip().splitlines()[0]}: {key}")
        return key

    def _get_latest_key_time(self, branch: str, key: str) -> int | None:
        branch_ref = self.repo.branches[branch]
        # Get all commits that modified the file in this branch, starting from the most recent
        commits = list(
            self.repo.iter_commits(paths=key, max_count=1, rev=branch_ref.commit.hexsha)
        )
        if commits:
            dprint(
                f"latest commit of key {branch}/{key}: {commits[0].message.strip().splitlines()[0]}"
            )
            return self._get_commit_timestamp(commits[0])
        else:
            return None

    def _cherry_pick(self, commit: Commit):
        try:
            self.repo.git.cherry_pick(commit)
        except GitCommandError:
            self._add_all_to_index()
            self.repo.git.cherry_pick("--continue", "--no-edit")

    def _del_branch(self, branch: str):
        self.repo.git.branch("-D", branch)

    def _get_first_commit(self, branch: str) -> Commit:
        c = self._get_commits_since(None, branch)[0]
        dprint(f"first commit of branch {branch}: {c.message.strip().splitlines()[0]}")
        return c

    def _merge_branches_histories(
        self, local_branch: str, remote_branch: str, dst_branch: str
    ):
        """
        starting from LCA(local_branch, remote_branch): keep only commits, that lead to latest
        changes of file in this commit
        """

        lca_commit = self._get_lca(local_branch, remote_branch)
        if not lca_commit:
            # If no LCA, assume no common history: use the entire history (without initial)
            local_commits = self._get_commits_since(None, local_branch)[1:]
            remote_commits = self._get_commits_since(None, remote_branch)[1:]
        else:
            local_commits = self._get_commits_since(lca_commit, local_branch)
            remote_commits = self._get_commits_since(lca_commit, remote_branch)

        # use 2 pointer algorithm to merge histories
        local_idx = 0
        remote_idx = 0

        # switch to dst branch, where merged history will be constructed
        self._switch(dst_branch, force=True)
        if lca_commit:
            # move dst branch to lca commit
            self._reset(lca_commit)
        else:
            # if lca does not exist - checkout to initial empty commit
            self._reset(self._get_first_commit(local_branch))

        while local_idx < len(local_commits) or remote_idx < len(remote_commits):
            if local_idx >= len(local_commits):
                # only remote commits left
                select = "remote"
            elif remote_idx >= len(remote_commits):
                # only local commits left
                select = "local"
            else:
                # first process older commit of two
                local_time = self._get_commit_timestamp(local_commits[local_idx])
                remote_time = self._get_commit_timestamp(remote_commits[remote_idx])

                if local_time < remote_time:
                    # local commit is older
                    select = "local"
                else:
                    # remote commit is older
                    select = "remote"

            if select == "local":
                sel_commit = local_commits[local_idx]
                sel_branch = local_branch
                other_branch = remote_branch
                local_idx += 1
            else:
                sel_commit = remote_commits[remote_idx]
                sel_branch = remote_branch
                other_branch = local_branch
                remote_idx += 1
            dprint(f"processing commit {sel_commit.message.strip().splitlines()[0]}")

            # changed key in selected commit
            sel_key = self._extract_commit_key(sel_commit)

            # latest modification of `sel_key` in `sel_branch`
            sel_time = self._get_latest_key_time(sel_branch, sel_key)

            # latest modification of `sel_key` in other branch
            other_time = self._get_latest_key_time(other_branch, sel_key)

            # if selected commit leads to latest modification of key, then - keep this
            # commit in dst_branch
            # else drop this commit, because it will lead to outdated state anyway
            dprint("comare times: ", sel_time, other_time)
            if not sel_time:
                # actually - unreachable
                accept = True
            elif not other_time:
                accept = True
            elif sel_time > other_time:
                accept = True
            else:
                accept = False

            if accept:
                dprint("accepting")
                self._cherry_pick(sel_commit)
            else:
                dprint("rejecting")


def parse_args():
    parser = argparse.ArgumentParser(
        description="A simple configuration and node management tool.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init command
    parser_init = subparsers.add_parser("init", help="Initialize the repo")

    # set command
    parser_set = subparsers.add_parser("set", help="Set a key-value pair")
    parser_set.add_argument("key", help="The key to set")
    parser_set.add_argument("value", help="The value to assign to the key")

    # get command
    parser_get = subparsers.add_parser(
        "get", help="Get the value of a key at a specific commit"
    )
    parser_get.add_argument("key", help="The key to retrieve")
    parser_get.add_argument(
        "--commit",
        help="Commit hash to retrieve the value from (optional)",
        default="HEAD",
    )

    # delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a key")
    parser_delete.add_argument("key", help="The key to delete")

    # node commands
    parser_node_add = subparsers.add_parser("node", help="Manage nodes")
    node_subparsers = parser_node_add.add_subparsers(
        dest="node_command", help="Node subcommands"
    )

    # node add command
    parser_node_add_cmd = node_subparsers.add_parser(
        "add", help="Add a node at the given path"
    )
    parser_node_add_cmd.add_argument("name", help="Name of added node")
    parser_node_add_cmd.add_argument("repo", help="Repo url to the node to add")

    # node delete command
    parser_node_delete_cmd = node_subparsers.add_parser(
        "delete", help="Delete a node at the given path"
    )
    parser_node_delete_cmd.add_argument("name", help="Name of deleting node")

    # sync command
    parser_sync = subparsers.add_parser("sync", help="Sync changes with node")
    parser_sync.add_argument("name", help="Name of node to sync with")

    # sync-all command
    parser_sync_all = subparsers.add_parser(
        "sync-all",
        help="Sync changes with all added nodes",
    )

    # list command
    parser_list = subparsers.add_parser(
        "list",
        help="List keys ad directory",
    )
    parser_list.add_argument(
        "--dir",
        help="Subdirectory to list, default=.",
        default=".",
    )

    # history command
    parser_history = subparsers.add_parser(
        "history",
        help="Show history of changes for key",
    )
    parser_history.add_argument("key", help="Key to list history for")

    return parser.parse_args()


def main():
    args = parse_args()

    if args.command == "init":
        if KVStorage.create_repo():
            KVStorage().init()
        return

    kv = KVStorage()

    if args.command == "set":
        print(f"Setting {args.key} = {args.value}")
        kv.set(args.key, args.value)

    elif args.command == "get":
        k = kv.get(args.key, args.commit)
        if k is None:
            if args.commit:
                print(
                    f"key {args.key} does not exist in storage at commit {args.commit}"
                )
            else:
                print(f"key {args.key} does not exist in storage")
            sys.exit(1)
        else:
            print(k)

    elif args.command == "delete":
        print(f"Deleting key: {args.key}")
        if kv.delete(args.key):
            print("Deleted succesfully")
        else:
            print(f"key {args.key} does not exist in storage")
            sys.exit(1)

    elif args.command == "node":
        if args.node_command == "add":
            print(f"Adding node {args.name}: {args.repo}")
            kv.node_add(args.name, args.repo)
        elif args.node_command == "delete":
            print(f"Deleting node {args.name}")
            kv.node_delete(args.name)

    elif args.command == "sync":
        print(f"Syncronizing local history with remote {args.name}")
        kv.sync(args.name)

    elif args.command == "sync-all":
        print(f"Syncronizing local history with all remotes")
        kv.sync_all()

    elif args.command == "list":
        print(f"listing keys in subdirectory {args.dir}")
        kv.list_keys(args.dir)

    elif args.command == "history":
        print(f"Listing history for key {args.key}")
        kv.history(args.key)

    else:
        # No command provided
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
