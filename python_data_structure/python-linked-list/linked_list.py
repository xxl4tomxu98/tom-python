"""
============================================================================
Implementation Exercise: Singly Linked List
============================================================================

-------
Phase 1:
-------
1. Node and LinkedList initialization
2. Getting a node by its position
3. Adding a node to the list's tail
4. Adding a node to list's head
5. Removing the head node
6. Removing the tail node
7. Returning the list length

-------
Phase 2:
-------

1. Check whether the list contains_value a value
2. Inserting a node value into the list at a specific position
3. Updating a list node's value at a specific position
4. Removing a node value from the list at a specific position
5. Format the list as a string whenever `print()` is invoked
"""

# Phase 1

# TODO: Implement a Linked List Node class here


class Node:
    # TODO: Set the `_value` `_next` node instance variables
    def __init__(self, value):
        self._value = value
        self._next = None

# TODO: Implement a Singly Linked List class here


class LinkedList:
    # TODO: Set the `_head` node, `_tail` node, and list `_length` instance variables
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    # TODO: Implement the get_node method here
    def get_node(self, position):
        head = self._head
        next = head
        i = 0
        while i < position:
            if i == self._length:
                return None
            i += 1
            next = next._next

        return next

    # TODO: Implement the add_to_tail method here
    def add_to_tail(self, value):
        new_node = Node(value)
        if self._head == None:
            self._head = new_node
            self._tail = new_node
        else:
            head = self._head
            next = head
            while next._next:
                head = next
                next = next._next
            next._next = new_node
            self._tail = new_node
        self._length += 1

    # TODO: Implement the add_to_head method here
    def add_to_head(self, value):
        new_node = Node(value)
        if self._head == None:
            self._head = new_node
            self._tail = new_node
        else:
            head = self._head
            self._head = new_node
            new_node._next = head
        self._length += 1

    # TODO: Implement the remove_head method here

    def remove_head(self):
        if self._length == 0:
            return None
        elif self._length == 1:
            head = self._head
            self._tail = None
            self._head = None
            self._length = 0
            return head
        else:
            head = self._head
            self._head = self._head._next
            self._length -= 1
            return head

    # TODO: Implement the remove_tail method here

    def remove_tail(self):
        if self._length == 0:
            return self._head
        elif self._length == 1:
            tail = self._tail
            self._tail = None
            self._head = None
            self._length = 0
            return tail
        else:
            current = self._head
            next = current._next
            while next._next:
                self._tail = next
                next = next._next
            self._length -= 1
            return next

    # TODO: Implement the __len__ method here
    def __len__(self):
        return self._length

# Phase 2

    # TODO: Implement the contains_value method here
    def contains_value(self, target):
        current = self._head

        while current:
            if current._value == target:
                return True
            current = current._next
        return False

    # TODO: Implement the insert_value method here
    def insert_value(self, position, value):
        if position > self._length:
            return False
        elif position == 0:
            self.add_to_head(value)
        elif position == self._length:
            self.add_to_tail(value)
        else:
            new_node = Node(value)
            current = self._head
            next = current
            i = 0
            while i < position:
                current = next
                next = next._next
                i += 1
            current._next = new_node
            new_node._next = next
            self._length += 1

    # TODO: Implement the update_value method here

    def update_value(self, position, value):
        node = self.get_node(position)
        if node:
            node._value = value
            return True
        else:
            return False

    # TODO: Implement the remove_node method here

    def remove_node(self, position):
        if position > self._length:
            return None
        elif position == 0:
            self.remove_head()
        elif position == self._length:
            self.remove_tail()
        else:
            current = self._head
            next = current
            i = 0
            while i < position:
                current = next
                next = next._next
                i += 1
            current._next = next._next
            self._length -= 1
            return next

    # TODO: Implement the __str__ method here
    def __str__(self):
        current = self._head
        if current == None:
            return "Empty List"
        values_string = ""
        values_string += current._value
        while current._next:
            current = current._next
            values_string += ", "
            values_string += current._value
        return values_string


# Phase 1 Manual Testing:


# 1. Test Node and LinkedList initialization
# node = Node('hello')
# print(node)                                     # <__main__.Node object at ...>
# print(node._value)                              # hello
# linked_list = LinkedList()
# <__main__.LinkedList object at ...>
# print(linked_list)

# # 2. Test getting a node by its position
# print(linked_list.get_node(0))                # None

# # 3. Test adding a node to the list's tail
#linked_list.add_to_tail('new tail node')
# print(linked_list.get_node(0))                # <__main__.Node object at ...>
# print(linked_list.get_node(0)._value)         # `new tail node`

# # 4. Test adding a node to list's head
#linked_list.add_to_head('new head node')
# print(linked_list.get_node(0))                # <__main__.Node object at ...>
# print(linked_list.get_node(0)._value)         # `new head node`

# # 5. Test removing the head node
# linked_list.remove_head()
# `new tail node` because `new head node` has been removed
# print(linked_list.get_node(0)._value)
# `None` because `new head node` has been removed
# print(linked_list.get_node(1))

# # 6. Test removing the tail node
# print(linked_list.get_node(0)._value)         # `new tail node`
# linked_list.remove_tail()
# print(linked_list.get_node(0))                # None

# # 7. Test returning the list length
# print(len(linked_list))                                 # 2

# Phase 2 Manual Testing
# # 1. Test whether the list contains_value a value
linked_list = LinkedList()
linked_list.add_to_head('new head node')
# print(linked_list.contains_value('new head node'))      # True
# print(linked_list.contains_value('App Academy node'))   # False

# # 2. Test inserting a node value into the list at a specific position
linked_list.insert_value(0, 'hello!')
print(linked_list.get_node(0)._value)                   # `hello!`

# # 3. Test updating a list node's value at a specific position
# linked_list.update_value(0, 'goodbye!')
# print(linked_list.get_node(0)._value)                   # `goodbye!`

# # 4. Test removing a node value from the list at a specific position
# print(linked_list.get_node(1)._value)                   # `new head node`
# linked_list.remove_node(1)
# print(linked_list.get_node(1))                          # None

# # 5. Format the list as a string whenever `print()` is invoked
new_linked_list = LinkedList()
print(new_linked_list)                  # Empty List
new_linked_list.add_to_tail('puppies')
print(new_linked_list)                  # puppies
new_linked_list.add_to_tail('kittens')
print(new_linked_list)                  # puppies, kittens
