#!/usr/bin/env python

import sys
from collections import defaultdict
#
# This program simply represents the identity function.
#

# we want to calculate the new ranks


alpha = 0.85

# def parseData():
prevId = -2

nodes = defaultdict(int)
for line in sys.stdin:
    # If the line starts with N as in NodeID:..., then we know it's passthrough information
    # and therefore just pass it on
    if line[0] == 'N':
        line1 = line[7:]
        sys.stdout.write(line1)
    elif line[0] == '#':
        #assert(len(splitLine) == 2)
        splitLine = line.split("\t")
        nodeId = splitLine[0][1:]
        sys.stdout.write("%s\t%f\n" % (nodeId, 0.15))
    else:
        # Now, if it's data of the form (node, amountOfRankToAddToNode)
        splitLine = line.split("\t")
        #assert(len(splitLine) == 2)
        nodeId = splitLine[0]
        rankChange = float(splitLine[1])
        nodes[nodeId] += rankChange 
       # totalRankChange += rankChange
                                   
for nodeId in nodes:
    #assert(nodeId != '')
    sys.stdout.write("%s\t%f\n" % (nodeId, alpha * nodes[nodeId] + (1-alpha) ))
# parseData()
