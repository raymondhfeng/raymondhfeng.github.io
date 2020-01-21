from Stack import Stack

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		self.nbr = None

class Tree:
	def __init__(self, root):
		self.root = root

	def __str__(self):
		result = []
		def helper(root):
			nonlocal result
			result += [(root.val, root.nbr.val if root.nbr else root.nbr)]
			if root.left:
				helper(root.left)
			if root.right:
				helper(root.right)
		helper(self.root)
		return str(result)

	def printTreePretty(self): #Prints the tree in a pretty way
		height = self.height()
		def processLayer(k, root):
			def helper(k, root, layer, layerNum):
				if k == 0:
					layer += [root.val]
					return layer
				else:
					if root.left:
						layer = helper(k-1,root.left,layer,layerNum)
					if root.right:
						layer = helper(k-1,root.right,layer,layerNum)
				return layer

			return helper(k, self.root, [], k)
		
		for i in range(self.height()):
			print(processLayer(i, self.root))

	def inOrderRecur(self): # Returns the inOrder traversal, recursive implementation
		def helper(root):
			if not root.left and not root.right:
				return [root.val]
			elif root.left and not root.right:
				return helper(root.left) + [root.val]
			elif root.right and not root.left:
				return [root.val] + helper(root.right)
			else:
				return helper(root.left) + [root.val] + helper(root.right)
		return helper(self.root)

	def preOrderRecur(self): # Returns the preOrder traversal, recursive implementation
		def helper(root):
			if not root.left and not root.right:
				return [root.val]
			elif root.left and not root.right:
				return [root.val] + helper(root.left)
			elif not root.left and root.right:
				return [root.val] + helper(root.right)
			else:
				return [root.val] + helper(root.left) + helper(root.right)
		return helper(self.root)

	def postOrderRecur(self): # Returns the postOrder traversal, recursive implementation
		

	def printLevelOrder(self): # Prints the level order traversal 
		def printLayer(k, root):
			if k == 0:
				print(root.val)
			else:
				if root.left:
					printLayer(k-1,root.left)
				if root.right:
					printLayer(k-1,root.right)
		for i in range(self.height()+1):
			printLayer(i,self.root)



	def height(self): #A tree with just a leaf has height 0
		def helper(root):
			if not root:
				return 0
			else:
				return max(1+helper(root.left), 1+helper(root.right))
		return helper(self.root)

	def assignNbr(self):
		def helper(root, rightmost):
			if len(rightmost) != 0:
				root.nbr = rightmost[0]
				rightmost = rightmost[1:]
			if root.left and root.right:
				leftRecurRightmost = [root.left] + helper(root.left, rightmost)
				rightRecurRightmost = [root.right] + helper(root.right, leftRecurRightmost)
				return rightRecurRightmost
			elif root.left and not root.right:
				leftRecurRightmost = [root.left] + helper(root.left, rightmost)
				return leftRecurRightmost
			elif not root.left and root.right:
				rightRecurRightmost = [root.right] + helper(root.right, rightmost)
				return rightRecurRightmost
			else:
				return [root]

		return helper(self.root, [])

	def balanced(self):
		def helper(root): 
			if root.left == None and root.right == None:
				return (1, True)
			elif root.left == None:
				rightResult = helper(root.right)
				return (1+rightResult[0],rightResult[0]==1 or rightResult[0]==0)
			elif root.right == None:
				leftResult = helper(root.left)
				return (1+leftResult[0],leftResult[0]==1 or leftResult[0]==0)
			else:
				rightResult = helper(root.right)
				leftResult = helper(root.left)
				countDiff = abs(rightResult[0]-leftResult[0])
				diff = countDiff == 0 or countDiff == 1
				return (1+rightResult[0]+leftResult[0],leftResult[1] and rightResult[1] and diff)
		return helper(self.root)

	# # Populate a tree from a sorted array. Only valid when the tree is empty
	# def from_arr(self, arr):
		