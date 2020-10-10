class Node:
  def __init__(self, value):
    self._value = value
    self._parent = None
    self._children = []

  @property
  def value(self):
    return self._value

  @property
  def children(self):
    return self._children

  def add_child(self, node):
    if node not in self._children:
      self._children.append(node)
      node.parent = self

  def remove_child(self, node):
    if node in self._children:
      #self._children.pop(self._children.index(node))
      self._children.remove(node)
      node.parent = None


  @property
  def parent(self):
    return self._parent

  @parent.setter
  def parent(self, node):
    if node == self._parent:
      return
    if self._parent is not None:
      self._parent.remove_child(self)
    self._parent = node
    if node is not None:
      node.add_child(self)



  # recursive solution DFS
  def depth_search(self, value):
    if self.value == value:
      return self
    for child in self._children:
      result = child.depth_search(value)
      if result != None:
        return result
    return None

  # iterative solution using stack
  # def depth_search(self, value):
  #   stack = [self]
  #   while stack:
  #     node = stack.pop()
  #     if node.value == value:
  #       return node
  #     for child in self._children:
  #       stack.append(child)

  # def breadth_search(self, value):
  #   if self.value == value:
  #     return self
  #   for child in self._children:
  #     if child.value == value:
  #       return child
  #     result = child.breadth_search(value)
  #     if result != None:
  #       return result


  # BFS iterative solution using queue
  def breadth_search(self, value):
    queue = [self]
    while queue:
      node = queue.pop(0)
      if node.value == value:
        return node
      queue.extend(node._children)


  def __str__(self):
    return f"Node<{self._value}>"
