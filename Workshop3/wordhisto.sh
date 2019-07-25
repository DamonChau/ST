#!/bin/bash
if [ -z "$1" ];then
  echo "You need to pass at least a file"
  exit 0
fi

if [ ! -f "$1" ];then
    echo "$1 is not a file"
    exit 0
fi

if [ ! -z "$2" ]; then
   if [ ! -f "$2" ]; then
	echo "$2 is not a file"
	exit 0
   else
	python3 countWords.py "$1" "$2" | python3 histogram.py
	exit 0	
   fi
fi

python3 countWords.py "$1" | python3  histogram.py
