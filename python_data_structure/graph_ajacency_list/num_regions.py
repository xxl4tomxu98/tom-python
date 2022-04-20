graph1 = {
            'a': ['b'],
            'b': ['a'],
            'c': ['d'],
            'd': ['e', 'c'],
            'e': ['d'],
        }

graph2 = {
            'x': [],
            'y': [],
            'z': [],
        }


def num_regions(graph):
    visited = set()
    count = 0
    for node in graph:
        if(_depthFirstRecur(node, graph, visited)):
            count += 1
    return count


def _depthFirstRecur(node, graph, visited):
    if node in visited:
        return False
    visited.add(node)
    for neighbor in graph[node]:
        _depthFirstRecur(neighbor, graph, visited)
    return True

print(num_regions(graph2))


def numRegions(graph):
    visited = set()
    counter = 0

    for node in graph:
        queue = [node]
        if node not in visited:
            counter += 1
        while len(queue)!=0:
            curr = queue.pop(0)
            if curr in visited:
                continue
            visited.add(curr)
            for neighbor in graph[curr]:
                queue.append(neighbor)    
    return counter

print(numRegions(graph1))
print(numRegions(graph2))