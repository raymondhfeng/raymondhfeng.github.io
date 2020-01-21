class LLNode:
	def __init__(self, value, after=None):
		self.value = value
		self.after = after

class LinkedList:
	def __init__(self, head):
		self.head = head

	def append(self, value):
		head = self.head
		while head.after != None:
			head = head.after
		head.after = LLNode(value)

	def push(self, value):
		newHead = LLNode(value)
		newHead.after = self.head
		self.head = newHead

	def removeDuplicatesTempBuffer(self): 
		seenElements = set()
		runner = self.head.after
		trailer = self.head
		seenElements.add(trailer.value)
		while runner:
			if runner.value not in seenElements:
				seenElements.add(runner.value)
				trailer.after = runner
				trailer = runner
				runner = runner.after
			else:
				runner = runner.after
		trailer.after = runner

	def removeDuplicatesWithoutTempBuffer(self):
		def removeValue(head, value): #removes all instances of value starting at head
			while head and head.value == value:
				head = head.after
			if not head:
				return head
			else:
				trailer = head
				runner = head.after
				while runner:
					if runner.value != value:
						trailer.after = runner
						trailer = runner
					runner = runner.after
				trailer.after = runner
			return trailer
			
		head = self.head
		while head:
			head.after = removeValue(head.after, head.value)
			head = head.after


	def __str__(self):
		result = []
		pointer = self.head
		while pointer:
			result += [pointer.value]
			result += ["->"]
			pointer = pointer.after

		result += ["None"]
		return str(result)