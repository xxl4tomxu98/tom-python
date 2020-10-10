"""
View the full problem and run the test cases at:
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
from tree_node import TreeNode

def buildTree(preorder, inorder):
  """
  :type preorder: List[int]
  :type inorder: List[int]
  :rtype: TreeNode
  """
  if len(preorder)==0 and len(inorder)==0:
    return None
  root = TreeNode(preorder[0])
  root_ind = inorder.index(preorder[0])
  left_inorder = inorder[:root_ind]
  right_inorder = inorder[root_ind + 1:]
  left_preorder = [i for i in preorder if i in left_inorder]
  right_preorder = [i for i in preorder if i in right_inorder]
  root.left = buildTree(left_preorder, left_inorder)
  root.right = buildTree(right_preorder, right_inorder)
  return root

preorder_tree_values = [3,9,20,15,7]
inorder_tree_values = [9,3,15,20,7]
root_node = buildTree(preorder_tree_values, inorder_tree_values)
print(root_node)
print(root_node.left.value)   # 9
print(root_node.right.value)  # 20
# Returns the `root` node of the following binary tree:
#   3
#  / \
# 9  20
#   /  \
#  15   7
