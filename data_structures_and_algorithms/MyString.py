class String:
	def __init__(self, initial):
		self.str = list(initial)

	def unique(self): # returns true if all of the elements are unique.
		seen = set()
		for elem in self.str:
			if elem in seen:
				return False
			else:
				seen.add(elem)
		return True

	def unique_no_data_structures(self): # returns true if all of the elements are unique. doesn't use extra data structures
		for i in range(len(self.str)):
			for j in range(i+1,len(self.str)):
				if self.str[i] == self.str[j]:
					return False
		return True

	def reverse(self):
		temp = None
		for i in range(len(self.str)//2):
			temp = self.str[i]
			rightIndex = len(self.str) - i - 1
			self.str[i] = self.str[rightIndex]
			self.str[rightIndex] = temp

	def __str__(self):
		return "".join(self.str)

	def replace_spaces(self): # replaces all the ' ' with '%20'
		count = 0
		for elem in self.str:
			if elem == ' ':
				count += 1
		newLength = len(self.str) + 2*count
		result = [0]*newLength
		position = newLength - 1
		for i in range(len(self.str)):
			if self.str[len(self.str) - i - 1] == ' ':
				result[position] = '0'
				result[position - 1] = '2'
				result[position - 2] = '%'
				position -= 3
			else:
				result[position] = self.str[len(self.str) - i - 1] 
				position -= 1
		self.str = result

	def is_permutation_of(self, other):
		char_count1 = {}
		char_count2 = {}
		if len(self.str) != len(other):
			return False
		for i in range(len(self.str)):
			if self.str[i] in char_count1:
				char_count1[self.str[i]] += 1
			else:
				char_count1[self.str[i]] = 1
			if other[i] in char_count2:
				char_count2[other[i]] += 1
			else:
				char_count2[other[i]] = 1
		for key in char_count1:
			if key not in char_count2:
				return False
			elif char_count1[key] != char_count2[key]:
				return False
		return True

	def compress(self): # aabcccccaaa would become a2b1c5a3
		count = 0
		currChar = None
		for elem in self.str:
			if elem != currChar:
				currChar = elem
				count += 2
		if count >= len(self.str):
			return
		else:
			result = [0] * count
			rIndex = 0
			character = self.str[0]
			counter = 0
			for i in range(len(self.str)):
				if self.str[i] == character:
					counter += 1
				else:
					result[rIndex] = character
					result[rIndex+1] = str(counter)
					counter = 1
					rIndex += 2
					character = self.str[i]
			result[rIndex] = character
			result[rIndex+1] = str(counter)
		print(result)
		self.str = result

	def isSubstring(self, other): #returns true of this is a substring of other
		thisBuf = self.stringBuf()
		otherBuf = other.stringBuf()
		if len(thisBuf) > len(otherBuf):
			return False
		else:
			for i in range(len(otherBuf) - len(thisBuf) + 1):
				if otherBuf[i:i+len(thisBuf)] == thisBuf:
					return True
			return False


	def isRotation(self, other): #checks to see if "other" is a rotation of this string
		otherCopy1 = other.strCopy()
		otherCopy2 = other.strCopy()
		otherCopy1.concatEnd(otherCopy2)
		concatenated = otherCopy1
		print(concatenated)
		return self.isSubstring(concatenated)


	def strCopy(self): #returns a copy of this string object
		copy = String(self.str)
		return copy

	def stringBuf(self): #returns the string buffer that represents us
		return self.str

	def concatEnd(self, other): #concatenates "other" to the end of us
		self.str += other.stringBuf()

def main():
	print("Hello world!")
	str1 = String("gygomd")
	print(str1.unique_no_data_structures())
	print(str1.unique())
	str2 = String("raymond")
	print(str2.unique())
	print(str2.unique_no_data_structures())

	str1.reverse()
	print(str1)
	str2.reverse()
	print(str2)

	str3 = String("hi my name is raymond and i like turtles")
	str3.replace_spaces()
	print(str3)

	print(str1.is_permutation_of("dmogyg"))
	print(str1.is_permutation_of("gygomdg"))
	print(str1.is_permutation_of("gyggmd"))

	str4 = String("aabcccccaaa")
	str4.compress()
	print(str4)

	str5 = String("raymond")
	str6 = String("ray")
	str7 = String("mond")
	str8 = String("ymo")
	str9 = String("mondray")
	print(str6.isSubstring(str5))
	print(str7.isSubstring(str5))
	print(str8.isSubstring(str5))
	print(str9.isRotation(str5))
	print(str5.isRotation(str9))

if __name__ == "__main__":
	main()