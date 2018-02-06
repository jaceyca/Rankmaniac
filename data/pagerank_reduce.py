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
        assert(len(splitLine) == 2)
        splitLine = line.split("\t")
        nodeId = splitLine[0]
        degreeChange = float(splitLine[1])
        if prevId == None:
            prevId = nodeId
            totalDegreeChange += degreeChange
        elif prevId == nodeId:
            totalDegreeChange += degreeChange
        else: # we have a new ID
            # This might have to be (1-alpha)/ |N| in which case we need to keep track
            # of total number of nodes as passthrough information
            newDegree = alpha * totalDegreeChange + (1-alpha)   
            sys.stdout.write("%s, %f \n" % (nodeId, newDegree))
            totalDegreeChange = degreeChange
            prevId = nodeId
                                       
parseData()
                  
                  
                  
                  
                  
                  
                  
                  
                  