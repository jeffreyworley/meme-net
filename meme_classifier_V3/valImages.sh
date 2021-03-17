#!/usr/bin/env bash
find . -size 0 -print -delete
cd meme_img_set/train/
echo starting train
for d in */ ; do
	echo $d
  for f in $d*.jpg; do 
    djpeg -fast -grayscale -onepass $f > /dev/null;  
    if [ $? -ne 0 ]; then
      echo removing $f
      rm $f
    fi
  done
done
echo finished train starting test
cd ../test/
for d in */ ; do
	echo $d
  for f in $d*.jpg; do 
    djpeg -fast -grayscale -onepass $f > /dev/null;
    if [ $? -ne 0 ]; then
      echo removing $f
      rm $f
    fi
  done
done