#!/bin/bash


git switch -C master
git reset --hard 37be269
git switch -C remote
git reset --hard 37be269

git switch master
python3 ../kv.py set A 1
python3 ../kv.py set B 1

git switch remote
git reset --hard master

git switch master
python3 ../kv.py set A 2
git switch remote
python3 ../kv.py set A 3
git switch master
python3 ../kv.py set B 2

git switch master
git branch -D tmp


