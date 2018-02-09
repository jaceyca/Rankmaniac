#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

# we want to calculate the new ranks


alpha = 0.85

# def parseData():
prevId = -2
totalRankChange = 0.0
newRank = 0.0
for line in sys.stdin:
    # If the line starts with N as in NodeID:..., then we know it's passthrough information
    # and therefore just pass it on
    if line[0] == 'N':
        line = line[7:]
        sys.stdout.write(line)
    else:
        # Now, if it's data of the form (node, amountOfRankToAddToNode)
        splitLine = line.split("\t")
        #assert(len(splitLine) == 2)
        nodeId = splitLine[0]
        rankChange = float(splitLine[1])
        # If this is the first line
        if prevId == -2:
            prevId = nodeId
        elif prevId != nodeId:
            # we have a new ID
            newRank = alpha * totalRankChange + (1-alpha)   
            sys.stdout.write("%s\t%f\n" % (prevId, newRank))
            totalRankChange = 0.0
            prevId = nodeId
        totalRankChange += rankChange
if prevId != -2:
    newRank = alpha * totalRankChange + (1-alpha)   
    sys.stdout.write("%s\t%f\n" % (prevId, newRank))
                                   
# parseData()
