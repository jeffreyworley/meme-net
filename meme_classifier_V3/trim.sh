#!/usr/bin/env bash
find . -type d -print0 | while read -d '' -r dir; do
    files=("$dir"/*)
    printf "%5d files in directory %s\n" "${#files[@]}" "$dir"
    if [ ${#files[@]} -lt 20 ]
    then
    	echo removing $dir from train and test
    	rm -rf $dir 
    	rm -rf ../test/$dir
  	fi
done