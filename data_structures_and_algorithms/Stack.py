from LinkedList import LinkedList

class MinStack:
	def __init__(self): 
		self.arr = []

	def push(self, value):
		self.arr += [value]

	def pop(self):
		toReturn = self.arr[-1]
		self.arr = self.arr[:-1]
		return toReturn

	def peek(self):
		if len(self.arr) > 0:
			return self.arr[-1]
		else:
			raise Exception("stack is empty")

	def isEmpty(self):
		return len(self.arr) == 0

class Stack:
	def __init__(self): 
		self.arr = []
		self.minStack = None
		self.count = 0

	def push(self, value):
		if not self.minStack:
			self.minStack = MinStack()
			self.minStack.push(99999999)
		self.arr += [value]
		if value < self.minStack.peek():
			self.minStack.push(value)
		self.count += 1

	def pop(self):
		if self.isEmpty():
			raise Exception("Error: Stack is empty.")
		toReturn = self.arr[-1]
		self.arr = self.arr[:-1]
		if toReturn == self.minStack.peek():
			self.minStack.pop()
		self.count -= 1
		return toReturn

	def peek(self):
		if len(self.arr) > 0:
			return self.arr[-1]
		else:
			raise Exception("stack is empty")

	def isEmpty(self):
		return len(self.arr) == 0

	def min(self): #returns the minimum of the stack
		return self.minStack.peek()

	def numElems(self):
		return self.count

	def sort(self): #sorts the stack with only one auxilliary stack. large items deep and small items shallow
		aux = Stack()
		temp = None
		while not self.isEmpty():
			temp = self.pop()
			if aux.isEmpty():
				aux.push(temp)
			else:
				count = 0
				while not aux.isEmpty() and aux.peek() > temp:
					count += 1
					self.push(aux.pop())
				aux.push(temp)
				for _ in range(count):
					aux.push(self.pop())

		while not aux.isEmpty():
			self.push(aux.pop())

	def __str__(self):
		return "bottom" + str(self.arr) + "top"

class SetOfStacks:
	def __init__(self, capacity):
		self.capacity = capacity
		self.list = [Stack()] # recent in front, oldest in back

	def push(self, val):
		currStack = self.list[0]
		if currStack.numElems() >= self.capacity:
			self.list = [Stack()] + self.list
			currStack = self.list[0]
			currStack.push(val)
		else:
			currStack.push(val)

	def pop(self):
		currStack = self.list[0]
		if len(self.list) == 1:
			return currStack.pop()
		else:
			if currStack.isEmpty():
				self.list = self.list[1:]
			return self.list[0].pop()

	def popAt(self, index):
		currStack = self.list[index]
		result = currStack.pop()
		if currStack.isEmpty():
			self.list = self.list[:index] + self.list[index+1:]
		return result

	def __str__(self):
		result = ""
		for i in range(len(self.list)):
			result += "stack #" + str(i)
			result += str(self.list[i])
			result += "\n"
		return result

class Queue:
	def __init__(self):
		self.frontStack = Stack() #the stack that represents the front of the queue
		self.backStack = Stack() #the stack that represents the back of the queue
		self.isFront = True 

	def enqueue(self, elem):
		if self.isFront: #need to move all items to the back queue
			while not self.frontStack.isEmpty():
				self.backStack.push(self.frontStack.pop())
			self.isFront = not self.isFront
		self.backStack.push(elem)

	def dequeue(self):
		if not self.isFront:
			while not self.backStack.isEmpty(): #need to move all items to the front queue
				self.frontStack.push(self.backStack.pop())
			self.isFront = not self.isFront
			return self.frontStack.pop()

	def __str__(self):
		result = ""
		if self.isFront:
			result += "back"
			result += str(self.frontStack)
			result += "front"
		else:
			result += "front"
			result += str(self.backStack)
			result += "back"
		return result

def main():
	stack1 = Stack()
	for i in range(10):
		stack1.push(10-i)
	print(stack1)
	print(stack1.min())
	stack1.pop()
	print(stack1)
	print(stack1.min())

	queue1 = Queue()
	for i in range(10):
		queue1.enqueue(i)
	print(queue1)
	queue1.dequeue()
	print(queue1)
	queue1.enqueue(99)
	print(queue1)

	stack2 = Stack()
	stack2.push(3)
	stack2.push(5)
	stack2.push(1)
	stack2.push(0)
	stack2.push(7)
	stack2.push(2)
	stack2.push(9)
	print(stack2)
	stack2.sort()
	print(stack2)

	sos = SetOfStacks(5)
	for i in range(30):
		sos.push(i)
	print(sos)
	for i in range(31):
		print(i)
		print(sos)
		sos.pop()
	print(sos)

if __name__ == "__main__":
	main()