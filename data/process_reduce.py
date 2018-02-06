#!/usr/bin/env python

import sys
import heapq

SIZE_OF_QUEUE = 20
#
# This program simply represents the identity function.
#
def parseData():
    # New Rank line: (id \t newRank)
    # Paassthrough line: (id \t iteration, current, neighbors)

    prevNode = None
    nodeStrings = {}
    isConverged = True

    priorityQueue = []
    for line in sys.stdin:
        splitLine = line.split("\t")
        nodeId = splitLine[0]
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

    while priorityQueue:
        rank, nodeId = heapq.heappop(priorityQueue)
        previousRanking = nodeStrings[nodeId][1]
        nodeStrings[nodeId][1] = currentRanking

        newTopKNodes.add(nodeId)

        topKRanks.append((rank, nodeId))

        if isConverged and currentRanking != previousRanking:
            isConverged = False
        currentRanking -= 1

    if isConverged:
        for i in range(SIZE_OF_QUEUE - 1, -1, -1):
            print(i, "!!!!\n\n")
            sys.stdout.write("FinalRank:%f\t%s" % (topKRanks[i][0], topKRanks[i][1]))
    else: 
        for nodeId in nodeStrings:
            outlinksString = ",".join(nodeStrings[nodeId][3:])
            if nodeId not in newTopKNodes:
                sys.stdout.write("NodeID:%s\t%i,%s,%s\n" % (nodeStrings[nodeId][0], -1, nodeStrings[nodeId][2], outlinksString))
            else:
                sys.stdout.write("NodeID:%s\t%i,%s,%s\n" % (nodeStrings[nodeId][0], nodeStrings[nodeId][1], \
                    nodeStrings[nodeId][2], outlinksString))
        
parseData()