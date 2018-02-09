#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

# we want to calculate the new ranks


alpha = 0.85

# def parseData():
prevId = -2

nodes = {}
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
        if prevId != nodeId:
            # we have a new ID
            nodes[nodeId] = rankChange 
            #sys.stdout.write("%s\t%f\n" % (prevId, newRank))
            #totalRankChange = 0.0
            prevId = nodeId
        else:
            nodes[nodeId] += rankChange 
       # totalRankChange += rankChange
                                   
for nodeId in nodes:
    sys.stdout.write("%s\t%f\n" % (nodeId, alpha * nodes[nodeId] + (1-alpha) ))
# parseData()
