class Queue:
	def __init__(self):
		self.arr = [] #Push to the back and pop from the front

	def enqueue(self, value):
		self.arr = self.arr + [value]

	def dequeue(self, value):
		result = self.arr[0]
		self.arr = self.arr[1:]
		return result