#!/usr/bin/env python

import sys
import heapq

SIZE_OF_QUEUE = 30
#
# This program simply represents the identity function.
#
# def parseData():
# New Rank line: (nodeId \t newRank)
# Paassthrough line: (nodeId \t iteration, current, neighbors)

prevNode = None
nodeStrings = {}

priorityQueue = []
for line in sys.stdin:
    splitLine = line.split("\t")
    nodeId = int(splitLine[0])
    assert(nodeId is not None)
    data = splitLine[1].strip().split(",")

    # Checking if this is [NodeID, new rank] line
    if len(data) == 1:
        curRank = float(data[0])
        if len(priorityQueue) < SIZE_OF_QUEUE:
            heapq.heappush(priorityQueue, (curRank, nodeId))
        else:
            heapq.heappushpop(priorityQueue, (curRank, nodeId))
    else:
        # From data = [iteration, current, neighbors]
        iteration = int(data[0])
        neighbors = data[2:]
    if nodeId == prevNode:
        nodeStrings[nodeId] = [nodeId, iteration, curRank] + neighbors
    else:
        prevNode = nodeId

    # For each line, we need to pass on the information of previous, the current iteration,
    # and neighbors

currentRanking = SIZE_OF_QUEUE
topKRanks = []
newTopKNodes = set()
isConverged = None

while priorityQueue:
    rank, nodeId = heapq.heappop(priorityQueue)
    previousRanking = nodeStrings[nodeId][1]
    nodeStrings[nodeId][1] = currentRanking

    newTopKNodes.add(nodeId)

    topKRanks.append((rank, nodeId))

    if currentRanking != previousRanking:
        isConverged = False
    currentRanking -= 1

    if currentRanking == 0:
        if isConverged is not False:
            isConverged = True
        break

if isConverged:
    for i in range(SIZE_OF_QUEUE - 1, SIZE_OF_QUEUE - 21, -1):
        sys.stdout.write("FinalRank:%f\t%s\n" % (topKRanks[i][0], topKRanks[i][1]))
elif isConverged is False: 
    for nodeId in nodeStrings:
        new_rank = -1
        outlinksString = ",".join(nodeStrings[nodeId][3:])
        outlinksLength = len(outlinksString)
        if nodeId in newTopKNodes:
            new_rank = nodeStrings[nodeId][1]
        if outlinksLength == 0:
            sys.stdout.write("NodeId:%i\t%i,%f\n" % (nodeStrings[nodeId][0], new_rank, nodeStrings[nodeId][2]))
        else:
            sys.stdout.write("NodeId:%i\t%i,%f,%s\n" % (nodeStrings[nodeId][0], new_rank, nodeStrings[nodeId][2], outlinksString))
elif isConverged is None:
    # sys.stdout.write("WTF IS GOING ON!!!!!!!!!!!!!!!!\n\n\n\n")    
    pass     
# parseData()
