#!/bin/bash

python3 sysaudit.py \
	monitor \
	--watch ./watch-1 \
	--watch ./watch-2 \
	--ignore '*.swp' \
	--ignore '*.tmp' \
	--keep '.gitignore' \
	--track ./watch-1/track-1 \
	--track ./watch-1/track-2 \
	--repo audit_db
