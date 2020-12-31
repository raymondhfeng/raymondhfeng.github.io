# How do you remove from a bst?
import random

class BstNode:
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.count = 1

	def _display_aux(self):
		"""Returns list of strings, width, height, and horizontal coordinate of the root."""
		# No child.
		if self.right is None and self.left is None:
			line = '%s' % (str(self.key) + "(" + str(self.count) + ")")
			width = len(line)
			height = 1
			middle = width // 2
			return [line], width, height, middle

		# Only left child.
		if self.right is None:
			lines, n, p, x = self.left._display_aux()
			s = '%s' % (str(self.key) + "(" + str(self.count) + ")")
			u = len(s)
			first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
			second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
			shifted_lines = [line + u * ' ' for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

		# Only right child.
		if self.left is None:
			lines, n, p, x = self.right._display_aux()
			s = '%s' % (str(self.key) + "(" + str(self.count) + ")")
			u = len(s)
			first_line = s + x * '_' + (n - x) * ' '
			second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
			shifted_lines = [u * ' ' + line for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

		# Two children.
		left, n, p, x = self.left._display_aux()
		right, m, q, y = self.right._display_aux()
		s = '%s' % (str(self.key) + "(" + str(self.count) + ")")
		u = len(s)
		first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
		second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
		if p < q:
			left += [n * ' '] * (q - p)
		elif q < p:
			right += [m * ' '] * (p - q)
		zipped_lines = zip(left, right)
		lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
		return lines, n + m + u, max(p, q) + 2, n + u // 2

class Bst: # supports duplicate elements
	def __init__(self):
		self.root = None

	def isEmpty(self):
		return not self.root

	def insert(self, key):
		def helper(root, key):
			if key == root.key:
				root.count += 1
			elif key > root.key:
				if root.right:
					helper(root.right, key)
				else:
					root.right = BstNode(key)
			else:
				if root.left:
					helper(root.left, key)
				else:
					root.left = BstNode(key)
		if not self.root:
			self.root = BstNode(key)
		else:
			helper(self.root, key)

	def getRankOfNumber(self, key):
		def count(root):
			if not root:
				return 0
			elif not root.left and not root.right:
				return root.count
			elif not root.left and root.right:
				return root.count + count(root.right)
			elif not root.right and root.left:
				return root.count + count(root.left)
			else:
				return root.count + count(root.left) + count(root.right)
		def helper(root, key):
			if not root:
				return -1
			elif key == root.key:
				return count(root.left)
			elif key < root.key:
				return helper(root.left, key)
			else:
				if root.left:
					return count(root.left) + root.count + helper(root.right, key)
				else:
					return root.count + helper(root.right, key)


		return helper(self.root, key)


	def display(self):
		lines, _, _, _ = self.root._display_aux()
		for line in lines:
			print(line)

def main():
	tree = Bst()
	for i in range(10):
		tree.insert(random.randint(1,10))
	tree.display()

	print(tree.getRankOfNumber(5))
	
if __name__ == "__main__":
	main()
