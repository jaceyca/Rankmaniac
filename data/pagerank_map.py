#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

# we want to parse the data into usable components
    
def parseData():
    for line in sys.stdin:
        splitLine = line.split("\t")
        nodeId = splitLine[0].split(":")[1]
        data = splitLine[1].strip().split(",")
        # TODO: figure out how to not hardcode this
        if data[0] == "1.0":
            iteration = 0
            curr = float(data[0])
            prev = float(data[1])
            outlinks = data[2:]
        else:
            iteration = int(data[0])
            curr = float(data[1])
            prev = float(data[2])
            outlinks = data[3:]
            
        outlinksString = ",".join(outlinks)
        if len(outlinks) == 0:
            sys.stdout.write("%s, %f \n" % (nodeId, curr))
        else:
            for neighbor in outlinks:
                sys.stdout.write("%s, %f \n" % (neighbor, curr/len(outlinks)))
        # sys.stdout.write("nodeId: %s, iteration: %i, curr: %f, prev: %f, outlinks: %s \n" % (nodeId, iteration, curr, prev, outlinksString))
        
parseData()
