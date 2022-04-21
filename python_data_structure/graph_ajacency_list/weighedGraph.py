from functools import reduce
import math
graph = {
    'a': { 'c': 1, 'b': 7 },
    'b': { 'a': 7, 'd': 12, 'e': 13 },
    'c': { 'a': 1, 'd': 20, 'f': 4 },
    'd': { 'b': 12, 'c': 20, 'e': 5 },
    'e': { 'b': 13, 'd': 5, 'f': 9 },
    'f': { 'c': 4, 'e': 9 }
}


def dijkstras(graph, source):
    #use dict to represent min distances between source and other nodes
    distance = {}
    #initialize all nodes to be Infinity distance away from the source
    for node in graph:
        distance[node] = math.inf
    
    # the source is 0 distance away from itself
    distance[source] = 0

    # initialize all nodes to be unvisited
    unvisited = set(graph.keys())
    # prepare an object to track the optimal paths
    previous = {}

    # while some nodes are still unvisited
    while (len(unvisited) > 0):
        #find the closest unvisited node
        currNode = minDistanceNode(unvisited, distance)
        #and mark it as visited
        unvisited.remove(currNode)
        # consider all neighbors of the current node
        for neighbor in graph[currNode]:
            #calculate the total distance of the neighbor
            # if we travel through the current node to get to that neighbor
            distanceFromCurrToNeighbor = graph[currNode][neighbor]
            totalNeighborDistance = distance[currNode] + distanceFromCurrToNeighbor
            # if the total distance is better than the old distance we calculated for neighbor,
            if distance[neighbor] > totalNeighborDistance:
                # then replace it
                distance[neighbor] = totalNeighborDistance
                # and now we say that the optimal path has `currNode` followed by `neighbor`
                previous[neighbor] = currNode
    
    return (distance, previous)
       

# this helper function will find the unvisited node with the smallest distance
def minDistanceNode(nodes, distance):
    return reduce(lambda node, minNode: node if distance[node] < distance[minNode] else minNode, nodes)
         

(distance, previous) = dijkstras(graph, 'a')
print(distance)
print(previous)