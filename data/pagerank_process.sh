#!/bin/bash
PYVERSION=python2.7 # Change this to however you invoke python
COUNT=0
while [ $COUNT -lt 50 ];
do
$PYVERSION pagerank_map.py < input.txt | sort | $PYVERSION pagerank_reduce.py |
$PYVERSION process_map.py | sort | $PYVERSION process_reduce.py > output.txt
((COUNT++))
done
