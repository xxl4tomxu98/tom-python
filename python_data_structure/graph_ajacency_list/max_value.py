import math

graph = {
    5: [3, 2, 4],
    3: [2],
    2: [7, 10],
    4: [],
    6: [7],
    7: [10],
    10:[]
}


def max_value_recur(node, graph, visited=set()):
    if node in visited:
        #visited node should never get picked via comparison
        return -math.inf
    if not graph[node]:
        return node
    print(node)
    visited.add(node)
    neighborMax = []       
    for neighbor in graph[node]:        
        neighborMax.append(max_value_recur(neighbor, graph, visited))
    return max(node, *neighborMax)

#print(max_value_recur(5, graph))


def max_value_iter(node, graph, visited=set()):
    stack = [node]
    currMax = node
    while len(stack)!=0:
        num = stack.pop()
        if num in visited:
            #visited node should never get picked via comparison
            continue    
        print(num)
        visited.add(num)
        if num > currMax:
            currMax = num      
        for neighbor in graph[num]:        
            stack.append(neighbor)
    return currMax

print(max_value_iter(5, graph))


def maxValueRecur(node, graph, visited= set()):    
    if (node in visited):
        return
    print(node)  
    visited.add(node)
    for neighbor in graph[node]:    
        return maxValueRecur(neighbor, graph, visited)
    return max(*list(visited))

#print(maxValueRecur(5, graph))

def maxValueIter(node, graph, visited=set()):
    queue = [node]
    currMax = node
    while len(queue)!=0:
        num = queue.pop(0)
        if num in visited:
            #visited node should never get picked via comparison
            continue    
        print(num)
        visited.add(num)
        if num > currMax:
            currMax = num      
        for neighbor in graph[num]:        
            queue.append(neighbor)
    return currMax

print(maxValueIter(5, graph))


