#!/usr/bin/env python

import sys
import numpy as np

#
# This program simply represents the identity function.
#

# we want to calculate the new ranks

alpha = 0.85

def parseData():
    prevId = None
    values = []
    for line in sys.stdin:
        splitLine = line.split(",")
        nodeId = splitLine[0]
        value = float(splitLine[1])
        
        if prevId == None:
            prevId = nodeId
            values.append(value)
        elif nodeId == prevId:
            values.append(value)
        else:
            calculateSum(prevId, values)
            prevId = nodeId
            values = [value]
                                
def calculateSum(nodeId, values):
    values_sum = np.sum(values)
    curr = alpha * values_sum + (1-alpha)
    sys.stdout.write("%s, %f \n" % (nodeId, curr))

                  
parseData()
                  
                  
                  
                  
                  
                  
                  
                  
                  