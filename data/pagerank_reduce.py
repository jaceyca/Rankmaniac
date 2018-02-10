#!/usr/bin/env python

import sys

totalRanks = {}
newRank = 0.0

for line in sys.stdin:
    if line[0] == '#':
        sys.stdout.write(line)
    elif line[0] == ':':
        sys.stdout.write(line[1:])
    elif line[0] == '!':
        splitLine = line.split("\t")
        nodeId = splitLine[0][1:]
        sys.stdout.write("%s\t%f\n" % (nodeId, 0.15))
    else:
        splitLine = line.split("\t")
        nodeId = splitLine[0]
        rankChange = float(splitLine[1])
        if nodeId in totalRanks:
            totalRanks[nodeId] = totalRanks[nodeId] + rankChange
        else:
            totalRanks[nodeId] = rankChange
for nodeId in totalRanks:
    new_rank = 0.85 * totalRanks[nodeId] + 0.15
    sys.stdout.write("%s\t%f\n" % (nodeId, new_rank))
