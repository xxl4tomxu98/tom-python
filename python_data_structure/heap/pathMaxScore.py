'''Suppose we have a matrix A of integers with R rows and C columns, we have to find 
the maximum score of a path starting from [0,0] and ending at [R-1,C-1]. Here the 
scoring technique will be the minimum value in that path. For example, the value of 
the path 8 → 4 → 5 → 9 is 4. A path moves some number of times from one visited cell
to any neighboring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

For example, if the grid is like:

5	4	5
1	2	6
7	4	6
The orange cells will be the path. The output is 4

To solve this, we will follow these steps 

r := number of rows and c := number of columns
ans := minimum of A[0, 0] and A[r - 1, c - 1]
make one matrix called visited of the order same as A, and fill this with FALSE
h := a list, where we store a tuple (-A[0, 0], 0, 0)
Make heap from h
while h is not empty
v, x, y := delete the h from heap, and store three values
if x = r - 1 and y := c - 1, then come out from loop
ans := min of ans, A[x, y]
visited[x, y] := true
for dy, dx in the list [(-1, 0), (1, 0), (0, 1), (0, -1)], do
a := x + dx and b := y + dy
if a in range 0 to r - 1 and b in range 0 to c - 1 and visited[a, b] is false,
insert (-A[a, b], a, b) into heap with h
return ans'''

import heapq


def maximumMinimumPath(A):
    """
    :type A: List[List[int]]
    :rtype: int
    """
    r,c = len(A),len(A[0])
    ans = min(A[0][0],A[-1][-1])
    visited = [[False for i in range(c)] for j in range(r)]
    h = [(-A[0][0],0,0)]
    heapq.heapify(h)
    while h:
        # print(h)
        v,x,y = heapq.heappop(h)
        if x== r-1 and y == c-1:
            break
        ans = min(ans,A[x][y])
        visited[x][y]= True
        for dx, dy in {(-1,0),(1,0),(0,1),(0,-1)}:
            a, b = x+dx, y+dy
            if a>=0 and a<r and b>=0 and b<c and not visited[a][b]:
                heapq.heappush(h,(-A[a][b],a,b))
    return ans


print(maximumMinimumPath([[5,4,5],[1,2,6],[7,4,6]]))
print(maximumMinimumPath([[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]))
print(maximumMinimumPath([[2,2,1,2,2,2],[1,2,2,2,1,2]]))
print(maximumMinimumPath([[5,4,5],[1,2,6],[7,4,6]]))