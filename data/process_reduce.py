#!/usr/bin/env python

import sys
import heapq

SIZE_OF_QUEUE = 20
NUM_ITERATIONS = 15
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
    else:
        # From data = [iteration, current, neighbors]
        iteration = int(data[0])
        neighbors = data[2:]

    if nodeId == prevNode:
        if iteration == NUM_ITERATIONS:
            if len(priorityQueue) < SIZE_OF_QUEUE:
                heapq.heappush(priorityQueue, (curRank, nodeId))
            else:
                heapq.heappushpop(priorityQueue, (curRank, nodeId))
        nodeStrings[nodeId] = [nodeId, iteration, curRank] + neighbors
    else:
        prevNode = nodeId

if iteration == NUM_ITERATIONS:
    currentRanking = SIZE_OF_QUEUE
    topKRanks = []

    while priorityQueue:
        rank, nodeId = heapq.heappop(priorityQueue)
        topKRanks.append((rank, nodeId))

        currentRanking -= 1


    for i in range(SIZE_OF_QUEUE - 1, SIZE_OF_QUEUE - 21, -1):
        sys.stdout.write("FinalRank:%f\t%s\n" % (topKRanks[i][0], topKRanks[i][1]))

else: 
    for nodeId in nodeStrings:
        outlinksString = ",".join(nodeStrings[nodeId][3:])
        outlinksLength = len(outlinksString)
        firstThree = nodeStrings[nodeId][0:3]
        if outlinksLength == 0:
            sys.stdout.write("NodeId:%i\t%i,%f\n" % (firstThree[0], firstThree[1], firstThree[2]))
        else:
            sys.stdout.write("NodeId:%i\t%i,%f,%s\n" % (firstThree[0], firstThree[1], firstThree[2], outlinksString))

