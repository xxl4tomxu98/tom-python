"""
View the full problem and run the test cases at:
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""
from bst import BinarySearchTree

class TreeNode(object):
  def __init__(self, value=0, left=None, right=None):
    self._value = value
    self._left = left
    self._right = right


def sortedArrayToBST(nums):
  """
  :type nums: List[int]
  :rtype: TreeNode
  """
  if len(nums) == 0:
    return None
  median = len(nums)//2

  node = TreeNode(nums[median])

  tree = BinarySearchTree(median)

  tree._root = node

  tree._root._left = sortedArrayToBST(nums[:median])
  tree._root._right = sortedArrayToBST(nums[median+1:])
  return tree._root


bst_root = sortedArrayToBST([-10,-3,0,5,9])

print(bst_root._value)               # 0
print(bst_root._left._value)          # -3
print(bst_root._left._left._value)     # -10
print(bst_root._right._value)         # 9
print(bst_root._right._left._value)    # 5
# Returns the root of the following binary search tree:
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
