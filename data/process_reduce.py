#!/usr/bin/env python

import sys
import heapq

SIZE_OF_QUEUE = 20
NUM_ITERATIONS = 2

# One line that is (iteration:\t $iter)
# $N lines that are (NodeId:$node \t $current, $neighbors)
# $N lines that are ($node \t $new_rank)

prevNode = -1
nodeStrings = {}
isConverged = False
iteration = 0
finalRanks = []

for line in sys.stdin:
    splitLine = line.split("\t")
    data = splitLine[1].strip().split(",")

    # This is (iteration:\t $iter)
    if splitLine[0][0] == "i":
        iteration = int(splitLine[1])
        # this is banking on the fact that iteration is the first line...
        if iteration >= NUM_ITERATIONS:
            isConverged = True
        else:
            sys.stdout.write("iteration:\t%i\n" % (iteration + 1))

    else:
        nodeId = int(splitLine[0])
        # This is ($node \t $new_rank)
        if len(data) == 1:
            new_rank = float(data[0])
        # This is (NodeId:$node \t $current, $neighbors)
        else:
            neighbors = data[1:]

        # If we have seen this node
        if nodeId == prevNode:
            # If we are done, create our final ranks
            if isConverged:
                if len(finalRanks) < SIZE_OF_QUEUE:
                    heapq.heappush(finalRanks, (new_rank, nodeId))
                else:
                    heapq.heappushpop(finalRanks, (new_rank, nodeId))
            nodeStrings[nodeId] = [str(nodeId), str(new_rank)] + neighbors
        else:
            prevNode = nodeId

# if this is the first iteration, emit a new iteration string
if iteration == 0:
    sys.stdout.write("iteration:\t2\n")

# we are done!
if isConverged:
    currentRanking = SIZE_OF_QUEUE
    topKRanks = []

    # we need to reverse the heap
    while finalRanks:
        new_rank, nodeId = heapq.heappop(finalRanks)
        # sys.stdout.write("newrank %s, nodeid %s \n" % (new_rank, nodeId))
        topKRanks.append((new_rank, nodeId))
        currentRanking -= 1
    # sys.stdout.write("size: %i \n" % len(topKRanks))

    for i in range(SIZE_OF_QUEUE - 1, SIZE_OF_QUEUE - 21, -1):
        sys.stdout.write("FinalRank:%s\t%s\n" % (topKRanks[i][0], topKRanks[i][1]))
# we are not done :(
else: 
    for nodeId in nodeStrings:
        outlinksString = ",".join(nodeStrings[nodeId][2:])
        outlinksLength = len(outlinksString)
        firstTwo = nodeStrings[nodeId][0:2]
        if outlinksLength == 0:
            sys.stdout.write("NodeId:%s\t%s\n" % (firstTwo[0], firstTwo[1]))
        else:
            sys.stdout.write("NodeId:%s\t%s,%s\n" % (firstTwo[0], firstTwo[1], outlinksString))

