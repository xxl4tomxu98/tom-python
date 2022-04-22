graph = {
    'a': ['b', 'c', 'e'],
    'b': [],
    'c': ['b', 'd'],
    'd': [],
    'e': ['a'],
    'f': ['e']
}


def breadthFirst(graph):
    visited = set()
    for node in graph:
        _breadthFirstIter(node, graph, visited)
            

def _breadthFirstIter(node, graph, visited):    
    queue = [node]
    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        print(node)
        visited.add(node)
        queue += graph[node]
    print(visited)


breadthFirst(graph)

