#!/usr/bin/env python

import sys
import heapq

SIZE_OF_QUEUE = 20
NUM_ITERATIONS = 15
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
        iteration = 0
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
            ''' if NUM_ITERATIONS == iteration:
                if len(priorityQueue) < SIZE_OF_QUEUE:
                    heapq.heappush(priorityQueue, (curRank, nodeId))
                else:
                    heapq.heappushpop(priorityQueue, (curRank, nodeId))'''
            nodeStrings[nodeId] = [nodeId, iteration, curRank] + neighbors
        else:
            prevNode = nodeId

        # For each line, we need to pass on the information of previous, the current iteration,
        # and neighbors

    if iteration == NUM_ITERATIONS:
    
        currentRanking = SIZE_OF_QUEUE
        topKRanks = []

        while priorityQueue:
            rank, nodeId = heapq.heappop(priorityQueue)
            topKRanks.append((rank, nodeId))
            currentRanking -= 1

        if isConverged:
            for i in range(SIZE_OF_QUEUE - 1, -1, -1):
                sys.stdout.write("FinalRank:%f\t%s\n" % (topKRanks[i][0], topKRanks[i][1]))
    else: 
        for nodeId in nodeStrings:
            outlinksString = ",".join(nodeStrings[nodeId][3:])
            outlinksLength = len(outlinksString)

            if outlinksLength == 0:
                sys.stdout.write("NodeId:%s\t%i,%s\n" % (nodeStrings[nodeId][0], nodeStrings[nodeId][1], nodeStrings[nodeId][2]))
            else:
                sys.stdout.write("NodeId:%s\t%i,%s,%s\n" % (nodeStrings[nodeId][0], nodeStrings[nodeId][1], nodeStrings[nodeId][2], outlinksString))
                
parseData()
