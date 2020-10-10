from tree_node import TreeNode

class BinarySearchTree:
  def __init__(self, value):
    self._root = None
    self._value = value
    self._left = None
    self._right = None

  # TODO: Implement node value insertion method
  def insert_value(self, value, current_node=False):
    if current_node == False:
      node = TreeNode(value)
      if self._root == None:
        self._root = node
        return self._root
      else:
        current_node = self._root
        if (value < current_node._value) and (current_node._left != None):
          current_node = current_node._left
        if (value >= current_node._value) and (current_node._right != None):
          current_node = current_node._right
        if (current_node._left == None) and (value < current_node._value):
          current_node._left = node
        if (current_node._right == None) and (value >= current_node._value):
          current_node._right = node



  # TODO: Implement iterative search method
  def search_iteratively(self, value):
    if self._root == None:
      return False
    current = self._root
    while current != None:
      if current._value == value:
        return True
      if current._value < value:
        current = current._right
      if current._value > value:
        current = current._left
    return False


  # TODO: Implement recursive search method
  def search_recursively(self, value, current_node=False):
    if self._root == None:
      return False
    if current_node == False:
      current_node = self._root
    if value < current_node._value:
      if current_node._left != None :
        current_node = current_node._left
      else:
        return False
    elif value > self._root._value:
      if current_node._right != None:
        current_node = current_node._right
      else:
        return False
    else:
      return True
    return self.search_recursively(value, current_node)




# tree = BinarySearchTree(3)
# print(tree._root)                         # None

# 1. Test node value insertion
# tree.insert_value(10)
# tree.insert_value(5)
# tree.insert_value(16)
# tree.insert_value(1)
# tree.insert_value(7)
# tree.insert_value(16)
# print(tree._root._value)                  # 10
# print(tree._root._left._value)            # 5
# print(tree._root._right._value)           # 16
# print(tree._root._left._left._value)      # 1
# print(tree._root._left._right._value)     # 7
# print(tree._root._right._right._value)    # 16

# # 2. Test iterative search
# empty_tree = BinarySearchTree(2)
# print(empty_tree.search_iteratively(10))  # False
# print(tree.search_iteratively(10))        # True
# print(tree.search_iteratively(7))         # True
# print(tree.search_iteratively(-1))        # False

# 3. Test recursive search
# print(empty_tree.search_recursively(10))  # False
# print(tree.search_recursively(10))        # True
# print(tree.search_recursively(7))         # True
# print(tree.search_recursively(-1))        # False
