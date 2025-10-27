#!/bin/bash


git switch -C master
git reset --hard 37be269
git switch -C remote
git reset --hard 37be269

git switch master
python3 ../kv.py set A 1

git branch -D remote
git checkout --orphan remote
git commit -m "Initial commit" -m "" -m "0"

python3 ../kv.py set A 2

git switch master
python3 ../kv.py set A 3

git switch remote
python3 ../kv.py set A 4

git switch remore
python3 ../kv.py set B 1

git switch master
git branch -D tmp


