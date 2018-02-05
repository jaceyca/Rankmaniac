#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

# we want to parse the data into usable components in this file

def parseData():
    for line in sys.stdin:
        splitLine = line.split("\t")
        nodeId = splitLine[0].split(":")[1]
        curr = splitLine[1].split(",")[0]
        prev = splitLine[1].split(",")[1]
        outlinks = splitLine[1].split(",")[2:]
    
        outlinksString = ",".join(outlinks)
        sys.stdout.write("nodeId:" + nodeId + " curr:" + curr + " prev:" + prev + " outlinks: " + outlinksString + "\n")
    
parseData()
