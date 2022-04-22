# convert a binary tree to BST keeping the same tree structure

# Program to convert binary tree to BST

# A binary tree node
class Node:
	
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Helper function to store the inorder traversal of a tree
def storeInorder(root, inorder):
	
	# Base Case
	if root is None:
		return
	
	# First store the left subtree
	storeInorder(root.left, inorder)
	
	# Copy the root's data
	inorder.append(root.data)

	# Finally store the right subtree
	storeInorder(root.right, inorder)

# A helper function to count nodes in a binary tree
def countNodes(root):
	if root is None:
		return 0

	return countNodes(root.left) + countNodes(root.right) + 1

# Helper function that copies contents of sorted array
# to Binary tree
def arrayToBST(arr, root):

	# Base Case
	if root is None:
		return
	
	# First update the left subtree
	arrayToBST(arr, root.left)

	# now update root's data delete the value from array
	root.data = arr[0]
	arr.pop(0)

	# Finally update the right subtree
	arrayToBST(arr, root.right)

# This function converts a given binary tree to BST
def binaryTreeToBST(root):
	
	# Base Case: Tree is empty
	if root is None:
		return
	
	# Count the number of nodes in Binary Tree so that
	# we know the size of temporary array to be created
	n = countNodes(root)

	# Create the temp array and store the inorder traversal
	# of tree
	arr = []
	storeInorder(root, arr)
	
	# Sort the array
	arr.sort()

	# copy array elements back to binary tree
	arrayToBST(arr, root)

# Print the inorder traversal of the tree
def printInorder(root):
	if root is None:
		return
	printInorder(root.left)
	print (root.data,end=" ")
	printInorder(root.right)

# Driver program to test above function
root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right = Node(5)

# Convert binary tree to BST
binaryTreeToBST(root)

print ("Following is the inorder traversal of the converted BST")
printInorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
