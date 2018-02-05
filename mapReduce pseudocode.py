def main():
    read input
    # input has (nodeId, current rank, previous rank, neighbors)

    # While reading input, read into adjacency lists
    adjacency = [[] for _ in range(len(input))]
    for i in input:
    	adjacency[nodeId] = neighbors

    previousRanks = [0 for _ in range(len(input))] 
    # Keep track of ranks for our stopping condition

    for i in range(50):
        pagerank_map(input)

        Collect, sort, and concatenate map outputs by key into
        listOfMapOutputs that contain tuples (neighbor, listOfDonatedRanks)

        pagerank_reduce(listOfMapOutputs)

        if (stoppingCondition):
            break



def pagerank_map(input, previousRanks):
    for node in input:
    	previousRanks[node] = current
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


def pagerank_reduce([neighbor, [donatedRanks]], previousRanks, adjacency):
    alpha = 0.85

    for neighbor in input:
        dotprod = sum(donatedRanks)

    return [neighbor, alpha * dotprod, previousRanks[neighbor], adjacency[neighbor]]

    
