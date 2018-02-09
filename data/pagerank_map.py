#!/usr/bin/env python

import sys

# Expected inputs:
# First iteration: (NodeId:$node \t $current, $prev, $neighbors)
# Every other iteration: 
# One line that is (iteration:\t $iter)
# Every other line is (NodeId:$node \t $current, $neighbors)

for line in sys.stdin:
    if line[0] == 'i':
        sys.stdout.write(line)
    else:
        splitLine = line.split("\t")
        nodeId = int(splitLine[0].split(":")[1])
        data = splitLine[1].strip().split(",")

        curr = float(data[0])
        # If this string has the previous rank
        if '.' in data[1]:
            outlinks = data[2:]
        else:
            outlinks = data[1:]
        
        outlinksString = ",".join(outlinks)

        lengthOutlinks = len(outlinks)
        # If there are no outlinks 
        if lengthOutlinks == 0:
            sys.stdout.write("%i\t%f\n" % (nodeId, curr))
            sys.stdout.write("NodeId:%i\t%f\n" % (nodeId, curr))
        else:
            for neighbor in outlinks:
                # For each neighbor, we need to pass on donated rank
                donated_rank = float(curr/lengthOutlinks)
                sys.stdout.write("%s\t%f\n" % (neighbor, donated_rank))
            sys.stdout.write("NodeId:%i\t%f,%s\n" % (nodeId, curr, outlinksString))

# Expect output:
# First iteration:
# $N lines that are ($node \t $donated_rank)
# $N lines that are (NodeId:$node \t $current, $neighbors)
# Every other:
# One line that is (iteration:\t $iter)
# $N lines that are ($node \t $donated_rank)
# $N lines that are (NodeId:$node \t $current, $neighbors)