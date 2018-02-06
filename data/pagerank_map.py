#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

# we want to parse the data into usable components
    
def parseData():
    # First line input: (id \t current, previous, neighbors)
    # Every other line: (id \t current, previous, iteration, neighbors)
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
            curr = float(data[0])
            prev = float(data[1])
            iteration = int(data[2])
            outlinks = data[3:]
            
        outlinksString = ",".join(outlinks)

        # For each line, we need to pass on the information of previous, the current iteration,
        # and neighbors
        sys.stdout.write("NodeID:%s \t %f, %i, %s\n" % (nodeId, curr, iteration, outlinks))

        # Other output is simply (node, amountOfRankToAddToNode)
        if len(outlinks) == 0:
            sys.stdout.write("%s \t %f \n" % (neighbor, curr))
        else:
            for neighbor in outlinks:
                sys.stdout.write("%s \t %f \n" % (neighbor, curr/len(outlinks)))
        # sys.stdout.write("nodeId: %s, iteration: %i, curr: %f, prev: %f, outlinks: %s \n" % (nodeId, iteration, curr, prev, outlinksString))
        
parseData()
