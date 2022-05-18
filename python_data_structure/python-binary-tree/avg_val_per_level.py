"""
Given a binary tree, get a list of average values for each level of the tree
Input:
    4
   / \ 
  7   9
 / \   \
10  2   6
     \
      6
     /
    2
output: [4, 8, 6, 6, 2]  
"""

from tree_node import TreeNode
# solution with O(n) time and space since we traverse all nodes and lists in dict
# values also occupy O(n) space
def dfs_traverse(node, hash, level=0):
    if not node:
        return None    
    if level not in hash:
        hash[level] = []                   
    hash[level].append(node.value)
    dfs_traverse(node.left, hash, level+1)
    dfs_traverse(node.right, hash, level+1)
    

def getAvgValues(node):
    hash = {}
    results = []    
    level = 0
    dfs_traverse(node, hash)
    while level in hash:        
        values = hash[level]
        print(values)
        results.append(sum(values)/len(values))
        level += 1
    return results



# solution with O(n) time since we traverse all nodes and avoid using lists in dict
# cause we use O(1) for space by using sum and count tuple for each key's values
def dfs_traverse1(node, hash, level=0):
    if not node:
        return None          
    if level not in hash:
        hash[level] = (node.value, 1)
    else:
        sum, count = hash[level]
        sum += node.value
        count += 1                
        hash[level] = (sum, count)
    dfs_traverse1(node.left, hash, level+1)
    dfs_traverse1(node.right, hash, level+1)


def getAvgValues1(node):
    hash = {}
    results = []    
    level = 0
    dfs_traverse1(node, hash)
    while level in hash:        
        sum, count = hash[level]
        print(sum, count)
        results.append(sum/count)
        level += 1
    return results


# solution with O(n) time since we traverse all nodes BFS and avoid using lists in dict
# we use O(1) for space by using sum and count tuple for each key's values and keep track of 
# level when pushing into queue so that at the start of each level I would reset sum and count
def bfs_traverse(node, hash):
    if not node:
        return None
    level = 0    
    queue = [(node, 0)]
    while queue:
        node, level = queue.pop(0)             
        if level not in hash:
            hash[level] = (node.value, 1)
        else:
            sum, count = hash[level]
            sum += node.value
            count += 1                
            hash[level] = (sum, count)
        if node.left:
            queue.append((node.left, level+1))
        if node.right:
            queue.append((node.right, level+1))


def getAvgValues_bfs(node):
    hash = {}
    results = []    
    level = 0
    bfs_traverse(node, hash)
    while level in hash:        
        sum, count = hash[level]
        print(sum, count)
        results.append(sum/count)
        level += 1
    return results


root = TreeNode(4)
b = TreeNode(7)
c = TreeNode(9)
d = TreeNode(10)
e = TreeNode(2)
f = TreeNode(6)
g = TreeNode(6)
h = TreeNode(2)

root.left = b
root.right = c
b.left = d
b.right = e
c.right = f
e.right = g
g.left = h


print(getAvgValues(root)) 
print(getAvgValues1(root))
print(getAvgValues_bfs(root))