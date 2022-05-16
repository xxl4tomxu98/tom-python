'''Number of groups formed in a graph of friends
Given n friends and their friendship relations, find the total number of groups that exist. 
And the number of ways of new groups that can be formed consisting of people from every 
existing group. If no relation is given for any person then that person has no group and 
singularly forms a group. If a is a friend of b and b is a friend of c, then a b and c form a group.

Examples:

Input : Number of people = 6
        Relations : 1 - 2, 3 - 4 and 5 - 6
Output: Number of existing Groups = 3
        Number of new groups that can
        be formed = 8
Explanation: The existing groups are
(1, 2), (3, 4), (5, 6). The new 8 groups
that can be formed by considering a
member of every group are (1, 3, 5),
(1, 3, 6), (1, 4, 5), (1, 4, 6), (2,
3, 5), (2, 3, 6), (2, 4, 5) and (2, 4, 6).

Input:  Number of people = 6
        Relations : 1 - 2 and 2 - 3
Output: Number of existing Groups = 2
        Number of new groups that can
        be formed = 3
Explanation: The existing groups are
(1, 2, 3) and (4). The new groups that
can be formed by considering a member
of every group are (1, 4), (2, 4), (3, 4).
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
To count number of groups, we need to simply count connected components in the given 
undirected graph. Counting connected components can be easily done using DFS or BFS.
Since this is an undirected graph, the number of times a Depth First Search starts from 
an unvisited vertex for every friend is equal to the number of groups formed.
To count number of ways in which we form new groups can be done using simply formula 
which is (N1)*(N2)*….(Nn) where Ni is the no of people in i-th group.
Time complexity: O(N + R) where N is the number of people and R is the number of relations.
'''



# Python3 program to count number of existing groups and number of new groups
# that can be formed. Note the class representation of graph adjacency list
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
    # Adds a relation as a two way edge of undirected graph.
    def addRelation(self, v, w):
        # Since indexing is 0 based,
        # reducing edge numbers by 1.
        v -= 1
        w -= 1
        self.adj[v].append(w)
        self.adj[w].append(v)

    # Returns count of not visited nodes reachable from v using DFS.
    def countUtil(self, v, visited):
        count = 1
        visited[v] = True
        i = 0
        while i != len(self.adj[v]):
            if (not visited[self.adj[v][i]]):
                count = count + self.countUtil(self.adj[v][i], visited)
            i += 1
        return count

    # A DFS based function to Count number
    # of existing groups and number of new
    # groups that can be formed using a
    # member of every group.
    def countGroups(self):
        # Mark all the vertices as
        # not visited
        visited = [0] * self.V
        existing_groups = 0
        new_groups = 1
        for i in range(self.V):
            # If not in any group.
            if (visited[i] == False):
                existing_groups += 1
                # Number of new groups that can be formed.
                new_groups = (new_groups * self.countUtil(i, visited))
        if (existing_groups == 1):
            new_groups = 0
        print("No. of existing groups are", existing_groups)
        print("No. of new groups that can be formed are", new_groups)

# Driver code
if __name__ == '__main__':

    n = 6

    # Create a graph given in the above diagram
    g = Graph(n) # total 6 people
    g.addRelation(1, 2) # 1 and 2 are friends
    g.addRelation(3, 4) # 3 and 4 are friends
    g.addRelation(5, 6) # 5 and 6 are friends

    g.countGroups()