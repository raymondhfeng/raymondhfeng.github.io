class Stack:
	def __init__(self): 
		self.arr = []

	def push(self, value):
		self.arr += [value]

	def pop(self):
		toReturn = self.arr[-1]
		self.arr = self.arr[:-1]
		return toReturn

	def empty(self):
		return len(self.arr) == 0

	def __str__(self):
		return str(self.arr)