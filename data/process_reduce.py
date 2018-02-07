#!/usr/bin/env python

import sys
import heapq
import numpy as np

SIZE_OF_QUEUE = 30
#
# This program simply represents the identity function.
#
def parseData():
    # New Rank line: (id \t newRank)
    # Paassthrough line: (id \t iteration, current, neighbors)

    diffs = []
    numNodes = 0
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
            prevRank = float(data[1])
        if nodeId == prevNode:

            #sumOfDiffs += (abs(curRank - prevRank))
            nodeStrings[nodeId] = [iteration, curRank, prevRank] + neighbors
            #numNodes += 1
        else:
            prevNode = nodeId

        # For each line, we need to pass on the information of previous, the current iteration,
        # and neighbors

    # avgDiff = sumOfDiffs / numNodes

    currentRanking = SIZE_OF_QUEUE
    topKRanks = []
    newTopKNodes = set()

    smallestDiffBetweenTopK = 999999
    prevNodeRank = -1

    while priorityQueue:
        newRank, nodeId = heapq.heappop(priorityQueue)
        #previousRanking = nodeStrings[nodeId][0]
        #nodeStrings[nodeId][0] = currentRanking
        prevRank = nodeStrings[nodeId][2]

        if prevNodeRank != -1:
            diff = abs(newRank - prevNodeRank)

            if diff < smallestDiffBetweenTopK:
                smallestDiffBetweenTopK = diff

        prevNodeRank = newRank

        diffs.append(abs(newRank - prevRank))

        #newTopKNodes.add(nodeId)

        topKRanks.append((newRank, nodeId))

        '''if isConverged and currentRanking != previousRanking:
            isConverged = False
        '''
        
        #currentRanking -= 1

    avgDiff = np.mean(diffs)
    stdDev = np.std(diffs)
    isConverged = (avgDiff + stdDev) < smallestDiffBetweenTopK

    if isConverged:
        for i in range(SIZE_OF_QUEUE - 1, SIZE_OF_QUEUE - 21, -1):
            sys.stdout.write("FinalRank:%f\t%s\n" % (topKRanks[i][0], topKRanks[i][1]))
        #sys.stdout.write("AvgDiff:%f\n" % avgDiff)
        #sys.stdout.write("StdDev:%f\n" % stdDev)
        #sys.stdout.write("SmallestDiff:%f\n" % smallestDiffBetweenTopK)
    else: 
        for nodeId in nodeStrings:
            new_rank = -1
            outlinksString = ",".join(nodeStrings[nodeId][3:])
            outlinksLength = len(outlinksString)
            '''
            if nodeId in newTopKNodes:
                new_rank = nodeStrings[nodeId][0]
            '''
            if outlinksLength == 0:
                sys.stdout.write("NodeId:%s\t%i,%s\n" % (nodeId, new_rank, nodeStrings[nodeId][1]))
            else:
                sys.stdout.write("NodeId:%s\t%i,%s,%s\n" % (nodeId, new_rank, nodeStrings[nodeId][1], outlinksString))
                
parseData()
