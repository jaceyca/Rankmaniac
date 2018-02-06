#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

# we want to calculate the new ranks


alpha = 0.85

def parseData():
    prevId = None
    totalDegreeChange = 0
    for line in sys.stdin:
        # If the line starts with N as in NodeID:..., then we know it's passthrough information
        # and therefore just pass it on
        if line[0] == 'N':
            sys.stdout.write(line)
            continue

        # Now, if it's data of the form (node, amountOfRankToAddToNode)
        splitLine = line.split("\t")
        assert(len(splitLine) == 2)
        nodeId = splitLine[0]
        degreeChange = float(splitLine[1])
        # If this is the first line
        if prevId == None:
            prevId = nodeId
            totalDegreeChange += degreeChange
        elif prevId == nodeId:
            totalDegreeChange += degreeChange
        else: # we have a new ID
            newDegree = alpha * totalDegreeChange + (1-alpha)   
            sys.stdout.write("%s\t%f\n" % (nodeId, newDegree))
            totalDegreeChange = degreeChange
            prevId = nodeId
                                       
parseData()
