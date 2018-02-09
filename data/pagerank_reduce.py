#!/usr/bin/env python

import sys

prevId = -2
totalRanks = {}
newRank = 0.0

# One line that is (# \t $iter)
# $N lines that are (:$node \t $current, $neighbors)
# $N lines that are ($neighbor \t $donated_rank)

for line in sys.stdin:
    # Pass on the iteration
    if line[0] == '#':
        sys.stdout.write(line)
    # Pass on NodeId string without NodeId
    elif line[0] == ':':
        sys.stdout.write(line[1:])
    else:
        # Now, if it's data of the form ($node \t $donated_rank)
        splitLine = line.split("\t")
        nodeId = int(splitLine[0])
        rankChange = float(splitLine[1])

        if nodeId in totalRanks:
            totalRanks[nodeId] = totalRanks[nodeId] + rankChange
        else:
            totalRanks[nodeId] = rankChange

for nodeId in totalRanks:
    new_rank = 0.85 * totalRanks[nodeId] + 0.15
    sys.stdout.write("%i\t%f\n" % (nodeId, new_rank))
                                   
# One line that is (# \t $iter)
# $N lines that are (:$node \t $current, $neighbors)
# $N lines that are ($node \t $new_rank)
