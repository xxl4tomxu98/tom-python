"""View the full problem and run the test cases at:
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take 
course 1, which is expressed as a pair: [0,1] Given the total number of courses and a list
of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible. The two courses are cycled loop

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. 
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5 """


def buildGraph(prerequisites):
    graph = {}
    for prerequisite in prerequisites:
        [course, pre] = [str(elem) for elem in prerequisite]
        if course in graph:
            graph[course].append(pre)
        else:
            graph[course] = [pre]
        if pre not in graph:
            graph[pre] = []
    return graph


def canFinish(numCourses, prerequisites):
    graph = buildGraph(prerequisites)
    totalCourses = len(graph.keys())
    # consider if I can visit all of the courses
    visited = set()
    eligibleCourses = True
    while(eligibleCourses):
        eligibleCourses = False
        for course in graph:
            #check all prerequisite requirements met?
            everyPreBeenMet = all([pre in visited for pre in graph[course]])
            if (course not in visited) & everyPreBeenMet:
                visited.add(course)
                eligibleCourses = True
    if len(visited) == totalCourses:
        return True
    else:
        return False



prerequisites = [[1,0], [0,2]]
print(buildGraph(prerequisites))
print(canFinish(3, prerequisites))


