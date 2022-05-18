"""Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm 
should work. You just need to ensure that a binary tree can be serialized to 
a string and this string can be deserialized to the original tree structure"""
from tree_node import TreeNode
def serialize(self, root):
    """Encodes a tree to a single string by DFS traversal.        
        :type root: TreeNode
        :rtype: str
    """
    my_str = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            my_str.append(f'{node.val},')
        else:
            # None node append null and return to beginning of loop
            # since there would be nothing to append to the stack
            my_str.append('null,')
            continue
        
        stack.append(node.right)
        stack.append(node.left)
    
    return ''.join(my_str)
    
def deserialize(self, data):
    """Decodes your encoded data to tree.    
        :type data: str
        :rtype: TreeNode
    """
    stack = data.split(',')
    # there is always a '' at the back after split
    # because when we do join it appends at the back too
    stack.pop()
    # reverse the list so we can just pop
    stk = stk[::-1]
    def helper():
        val = stack.pop()
        if val == 'null':
            return
        node = TreeNode(int(val))
        node.left = helper()
        node.right = helper()        
        return node
    return helper()