from Stack import Stack
from LinkedList import LinkedList, LLNode

class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		self.nbr = None

	def __str__(self):
		return str(self.val)

	def contains(self, node):
		if self == node:
				return True
		else:
			if self.left and self.right:
				return self.left.contains(node) or self.right.contains(node)
			elif self.left:
				return self.left.contains(node)
			elif self.right:
				return self.right.contains(node)
			else:
				return False

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

	def linkedListsOfLevels(self): #returns an array whose index contains the linked list of elements at that level
		levels = [None]*self.height()
		def helper(level, root):
			nonlocal levels
			if not levels[level]:
				levels[level] = LinkedList(LLNode(root.val))
			else:
				levels[level].append(root.val)
			if root.left:
				helper(level+1,root.left)
			if root.right:
				helper(level+1,root.right)
		helper(0,self.root)
		return levels

	# def postOrderRecur(self): # Returns the postOrder traversal, recursive implementation
		
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

	def firstCommonAncestor(self, this, that):
		def helper(root, this, that):
			if root.left and root.left.contains(this) and root.left.contains(that):
				return helper(root.left, this, that)
			elif root.right and root.right.contains(this) and root.right.contains(that):
				return helper(root.right, this, that)
			else:
				return root
		return helper(self.root, this, that)

	def isBst(self):
		def helper(root): # returns (min of subtree, max of subtree)
			if not root.left and not root.right:
				return (root.val, root.val, True)
			elif root.left and not root.right:
				leftResult = helper(root.left)
				bstBool = leftResult[2] and (leftResult[1] < root.val)
				return (leftResult[0] if leftResult[0] <= root.val else root.val, 
					leftResult[1] if leftResult[1] >= root.val else root.val, bstBool)
			elif not root.left and root.right:
				rightResult = helper(root.right)
				bstBool = rightResult[2] and (rightResult[0] > root.val)
				return (rightResult[0] if rightResult[0] <= root.val else root.val, 
					rightResult[1] if rightResult[1] >= root.val else root.val, bstBool)
			else:
				leftResult = helper(root.left) 
				rightResult = helper(root.right)
				bstBool = leftResult[2] and rightResult[2] and leftResult[1] < root.val and rightResult[0] > root.val
				subMin = min(leftResult[0],rightResult[0])
				subMax = max(leftResult[1],rightResult[1])
				return (subMin if subMin <= root.val else root.val, subMax if subMax >= root.val else root.val, bstBool)
		return helper(self.root)[2]


	# # Populate a tree from a sorted array. Only valid when the tree is empty
	# def from_arr(self, arr):

def main():
	# 			1
	# 		/		\
	# 	2				3
	#  /  \ 	      /   \
	# 4		5		6		7
	four = Node(4)
	five = Node(5)
	six = Node(6)
	seven = Node(7)
	three = Node(3, six, seven)
	two = Node(2, four, five)
	one = Node(1, two, three)
	t1 = Tree(one)
	print(t1.firstCommonAncestor(five, six))
	print(t1.firstCommonAncestor(six, seven))
	print(t1.firstCommonAncestor(three, five))
	print(t1.firstCommonAncestor(three, six))

	print(t1.isBst())

	a = Node(1)
	b = Node(5)
	c = Node(4,a,b)
	t2 = Tree(c)
	print(t2.isBst())

	d = Node(25)
	e = Node(10, None, d)
	f = Node(30)
	g = Node(20, e, f)
	t3 = Tree(g)
	print(t3.isBst())

	levels = t1.linkedListsOfLevels()
	for i in range(len(levels)):
		print(levels[i])


if __name__ == "__main__":
	main()
		