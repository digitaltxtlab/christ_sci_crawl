#!/bin/bash
# extract all files from subfolders to parent folder
# run in parent folder
find . -mindepth 2 -type f -print -exec mv {} . \;
