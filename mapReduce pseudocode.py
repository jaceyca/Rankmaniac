def main():
    read input
    # input has (nodeId, current rank, previous rank, neighbors)

    for i in range(50):
        pagerank_map(input)

        Collect, sort, and concatenate map outputs by key into
        listOfMapOutputs that contain tuples (neighbor, listOfDonatedRanks)

        pagerank_reduce(listOfMapOutputs)

        if (stoppingCondition):
            break



def pagerank_map(input):
    for node in input:
        if !iteration:
            iteration = 0
        else:
            if len(neighbors) > 0:
                for neighbor in neighbors:
                    # these neighbors will get the current node's rank
                    donated_rank = current / len(neighbors)
                    Emit(neighbor, donated_rank)
            else:
                Emit(node, current)


def pagerank_reduce([neighbor, [donatedRanks]]):
    alpha = 0.85

    for neighbor in input:
        dotprod = sum(donatedRanks)

    return [neighbor, alpha * dotprod]

