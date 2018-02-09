#!/usr/bin/env python

import sys
import heapq

SIZE_OF_QUEUE = 20
NUM_ITERATIONS = 17
prevNode = None
nodeStrings = {}
isConverged = False
iteration = 0
finalRanks = []

for line in sys.stdin:
    splitLine = line.split("\t")
    data = splitLine[1].strip().split(",")
    if splitLine[0][0] == "#":
        iteration = int(splitLine[1])
        if iteration >= NUM_ITERATIONS:
            isConverged = True
        else:
            sys.stdout.write("#\t%i\n" % (iteration + 1))
    else:
        nodeId = splitLine[0]
        if len(data) == 1:
            new_rank = float(data[0])
        else:
            neighbors = data[1:]
        if nodeId == prevNode:
            if isConverged:
                if len(finalRanks) < SIZE_OF_QUEUE:
                    heapq.heappush(finalRanks, (new_rank, nodeId))
                else:
                    heapq.heappushpop(finalRanks, (new_rank, nodeId))
            nodeStrings[nodeId] = [nodeId, str(new_rank)] + neighbors
        else:
            prevNode = nodeId
if iteration == 0:
    sys.stdout.write("#\t2\n")
if isConverged:
    currentRanking = SIZE_OF_QUEUE
    topKRanks = []
    while finalRanks:
        new_rank, nodeId = heapq.heappop(finalRanks)
        topKRanks.append((new_rank, nodeId))
        currentRanking -= 1

    for i in range(SIZE_OF_QUEUE - 1, SIZE_OF_QUEUE - 21, -1):
        sys.stdout.write("FinalRank:%s\t%s\n" % (topKRanks[i][0], topKRanks[i][1]))
else: 
    for nodeId in nodeStrings:
        outlinksString = ",".join(nodeStrings[nodeId][2:])
        firstTwo = nodeStrings[nodeId][0:2]
        if len(outlinksString) == 0:
            sys.stdout.write(":%s\t%s\n" % (firstTwo[0], firstTwo[1]))
        else:
            sys.stdout.write(":%s\t%s,%s\n" % (firstTwo[0], firstTwo[1], outlinksString))
