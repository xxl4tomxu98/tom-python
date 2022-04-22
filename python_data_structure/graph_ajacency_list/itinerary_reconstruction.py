'''Given a list of airline tickets represented by pairs of departure and arrival airports
[from, to], reconstruct the itinerary in order. All of the tickets belong to a man who 
departs from JFK. Thus, the itinerary must begin with JFK.'''
from typing import List
from collections import defaultdict


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    print(graph.keys(), graph.values())
    for key in graph:
        graph[key].sort()        
    stack = ['JFK']
    result = []
    while stack:
        if not graph[stack[-1]]:
            result.append(stack.pop())
        else:
            stack.append(graph[stack[-1]].pop(0))
    result.reverse()
    return result

print(findItinerary([['PHL','STL'], ['JFK','OHR'], ['LOG','STL'], ['OHR','PHL'], ['LOG', 'JFK']]))