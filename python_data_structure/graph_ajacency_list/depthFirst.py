graph = {
    'a': ['b', 'c', 'e'],
    'b': [],
    'c': ['b', 'd'],
    'd': [],
    'e': ['a'],
    'f': ['e']
}

graph2 = {
    'h': ['i', 'j'],
    'i': [],
    'j': ['k'],
    'k': [],
    'l': ['m'],
    'm': []
}


def depthFirst(graph):
    visited = set()
    for node in graph:
        _depthFirstIter(node, graph, visited)
        #_depthFirstRecur(node, graph, visited)


def _depthFirstIter(node, graph, visited):    
    stack = [node]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        print(node)        
        visited.add(node)
        stack += graph[node]


def _depthFirstRecur(node, graph, visited):    
    stack = [node]    
    node = stack.pop()
    if node in visited:
        return
    print(node)        
    visited.add(node)
    for neighbor in graph[node]:
        _depthFirstRecur(neighbor, graph, visited)

depthFirst(graph)
#depthFirst(graph2)
            
