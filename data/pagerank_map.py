#!/usr/bin/env python

import sys

for line in sys.stdin:
    if line[0] == '#':
        sys.stdout.write(line)
    else:
        splitLine = line.split("\t")
        nodeId = splitLine[0].split(":")[1]
        data = splitLine[1].strip().split(",")
        curr = data[0]
        if '.' in data[1]:
            outlinks = data[2:]
        else:
            outlinks = data[1:]
        outlinksString = ",".join(outlinks)
        lengthOutlinks = len(outlinks)
        if lengthOutlinks == 0:
            sys.stdout.write("%s\t%s\n" % (nodeId, curr))
            sys.stdout.write(":%s\t%s\n" % (nodeId, curr))
        else:
            for neighbor in outlinks:
                donated_rank = float(float(curr)/lengthOutlinks)
                sys.stdout.write("%s\t%f\n" % (neighbor, donated_rank))
            sys.stdout.write(":%s\t%s,%s\n" % (nodeId, curr, outlinksString))
