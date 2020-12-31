class LLNode:
	def __init__(self, value, after=None):
		self.value = value
		self.after = after

class LinkedList:
	def __init__(self, head):
		self.head = head

	def append(self, value):
		if self.head == None:
			self.head = LLNode(value)
		else:
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

	def findLoopStart(self):
		slow = self.head
		fast = self.head
		slow = slow.after
		fast = fast.after
		fast = fast.after
		counter = 1
		while slow != fast:
			slow = slow.after
			fast = fast.after
			fast = fast.after
			counter += 1
		fast = self.head
		while slow != fast:
			slow = slow.after
			fast = fast.after
		return slow

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

	def kthLastElement(self, k): # finds the kth to last element of a singly linked list
		slowRunner = self.head
		fastRunner = self.head
		for i in range(k):
			fastRunner = fastRunner.after
		while fastRunner:
			fastRunner = fastRunner.after
			if fastRunner:
				slowRunner = slowRunner.after

		return slowRunner.value

	def numRepresentation(self): #returns the linked list as if it was a digit in each node. LSD in front
		result = ""
		head = self.head
		while head:
			result = str(head.value) + result
			head = head.after
		return result

	@staticmethod
	def removeNode(node): #given just the node of a linked list, remove that node from the list
		node.value = node.after.value
		node.after = node.after.after

	@staticmethod
	def add(list1, list2): #least significant digits are at front of list
		head1 = list1.head
		head2 = list2.head
		carry = 0
		result = LinkedList(LLNode(-999999))
		while head1 or head2:
			if not head1 and head2:
				result.append(head2.value)
				head2 = head2.after
			elif head1 and not head2:
				result.append(head1.value)
				head1 = head1.after
			else:
				addResult = head1.value + head2.value + carry
				carry = addResult // 10
				result.append(addResult % 10)
			head1 = head1.after
			head2 = head2.after
		result.head = result.head.after
		return result

	def partitionByValue(self, val):
		less = None
		lessCurr = less
		geq = None
		geqCurr = geq
		head = self.head
		while head:
			print(head.value)
			if head.value < val:
				if not lessCurr:
					less = head
					lessCurr = less
				else:
					lessCurr.after = head
					lessCurr = lessCurr.after
			elif head.value >= val:
				if not geq:
					geq = head
					geqCurr = geq
				else:
					geqCurr.after = head
					geqCurr = geqCurr.after
			head = head.after
		self.head = less
		lessCurr.after = geq
		geqCurr.after = None

	def isPalindrome(self):
		reversed = LinkedList(None)
		head = self.head
		while head:
			reversed.push(head.value)
			head = head.after
		headCurr = self.head
		reversedCurr = reversed.head
		while headCurr:
			if not reversedCurr:
				return False
			if headCurr.value != reversedCurr.value:
				return False
			headCurr = headCurr.after
			reversedCurr = reversedCurr.after
		return True

	def __str__(self):
		result = []
		pointer = self.head
		while pointer:
			print(pointer.value)
			result += [pointer.value]
			result += ["->"]
			pointer = pointer.after

		result += ["None"]
		return str(result)

def main():
	zeroToTen = LinkedList(LLNode(0))
	for i in range(1,11):
		zeroToTen.append(i)
	print(zeroToTen)
	print(zeroToTen.kthLastElement(11))

	zero = LLNode(0)
	zeroToThree = LinkedList(zero)
	for i in range(1,3):
		zeroToThree.append(i)
	print(zeroToThree)
	LinkedList.removeNode(zero)
	print(zeroToThree)

	num1 = LinkedList(LLNode(9))
	num2 = LinkedList(LLNode(9))
	for i in range(1,9):
		num1.append(9-i)
		num2.append(9-i)
	print(num1.numRepresentation())
	print(num2.numRepresentation())
	additionResult = LinkedList.add(num1,num2)
	print(additionResult.numRepresentation())

	twelveToOne = LinkedList(None)
	for i in range(1,13):
		twelveToOne.append(13-i)
	print(twelveToOne)
	twelveToOne.partitionByValue(5)
	print(twelveToOne)

	oneToFive = LinkedList(None)
	palin = LinkedList(None)
	for i in range(1,5):
		oneToFive.push(6-i)
	palin.append(1)
	palin.append(3)
	palin.append(1)
	palin2 = LinkedList(None)
	palin2.append(6)
	print(oneToFive.isPalindrome())
	print(palin.isPalindrome())
	print(palin2.isPalindrome())

	fifteen = LLNode(15)
	fourteen = LLNode(14, fifteen)
	thirteen = LLNode(13, fourteen)
	twelve = LLNode(12, thirteen)
	eleven = LLNode(11, twelve)
	ten = LLNode(10, eleven)
	nine = LLNode(9, ten)
	eight = LLNode(8, nine)
	seven = LLNode(7, eight)
	six = LLNode(6, seven)
	five = LLNode(5, six)
	four = LLNode(4, five)
	three = LLNode(3, four)
	two = LLNode(2, three)
	one = LLNode(1, two)
	LL1 = LinkedList(one)

	fifteen.after = six
	
	loopStart = LL1.findLoopStart()
	print(loopStart.value)


if __name__ == "__main__":
	main()