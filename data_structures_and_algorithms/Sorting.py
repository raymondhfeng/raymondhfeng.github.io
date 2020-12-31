import string

def merge(A,B,alen): # Merges A and B, where B has enough space at the end to hold both
	aindex = alen - 1
	bindex = len(B) - 1
	aend = len(A) - 1
	while aindex >= 0 and bindex >= 0:
		if A[aindex] > B[bindex]:
			A[aend] = A[aindex]
			aindex -= 1
		else:
			A[aend] = B[bindex]
			bindex -= 1
		aend -= 1
	while aindex >= 0:
		A[aend] = A[aindex]
		aindex -= 1
		aend -= 1
	while bindex >= 0:
		A[aend] = B[bindex]
		bindex -= 1
		aend -= 1
	return A

def less_than_character_count(x, y):
	character_set = string.ascii_lowercase
	dict1 = {}
	dict2 = {}
	for elem in x:
		if elem in dict1:
			dict1[elem] += 1
		else:
			dict1[elem] = 1
	for elem in y:
		if y in dict2:
			dict2[elem] += 1
		else:
			dict2[elem] = 1
	for char in character_set:
		if char in dict1 and char in dict2:
			if dict1[char] < dict2[char]:
				return 1
			elif dict1[char] > dict2[char]:
				return -1
		elif char in dict1:
			return 1
		elif char in dict2:
			return -1
	return 0

class CircusPerson:
	def __init__(self, height, weight):
		self.height = height
		self.weight = weight
	def __lt__(self, other):
		return self.height < other.height and self.weight < other.weight
	def __gt__(self, other):
		return self.height > other.height and self.weight > other.weight
	def __eq__(self, other):
		return self.height == other.height and self.weight == other.weight
	def __le__(self, other):
		return self.height <= other.height and self.weight <= other.weight
	def __ge__(self, other):
		return self.height >= other.height and self.weight >= other.weight
	def __ne__(self, other):
		return self.height != other.height and self.weight == other.weight
	def __str__(self):
		return "("+str(round(self.height,1))+","+str(round(self.weight,1))+")"

from random import shuffle

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

def binary_search(A, val, lower, upper): #Performs binary search on a sorted array A
	# print("lower: ", lower)
	# print("upper: ", upper)
	if lower == upper and A[lower] != val:
		return -1
	midpoint = (upper + lower) // 2
	print("midpoint: ", midpoint)
	if A[midpoint] == val:
		return midpoint
	elif A[midpoint] > val:
		print("going left")
		return binary_search(A, val, lower, midpoint)
	else:
		print("going right")
		return binary_search(A, val, midpoint, upper)

def main():
	A = [1,3,5,7,9,0,0,0,0,0]
	B = [2,4,6,8,10]
	print(merge(A,B,5))

	str1 = "abcdefg"
	str2 = "gfedcba"
	print(less_than_character_count(str1,str2))
	print(less_than_character_count("a","aa"))
	print(less_than_character_count("ab","aa"))
	print(less_than_character_count("aab","bba"))

	def cmp_to_key(mycmp):
		# 'Convert a cmp= function into a key= function'
		class K:
			def __init__(self, obj, *args):
				self.obj = obj
			def __lt__(self, other):
				return mycmp(self.obj, other.obj) < 0
			def __gt__(self, other):
				return mycmp(self.obj, other.obj) > 0
			def __eq__(self, other):
				return mycmp(self.obj, other.obj) == 0
			def __le__(self, other):
				return mycmp(self.obj, other.obj) <= 0
			def __ge__(self, other):
				return mycmp(self.obj, other.obj) >= 0
			def __ne__(self, other):
				return mycmp(self.obj, other.obj) != 0
		return K

	L = ['foo', 'biology', 'sequence']
	L = [shuffle_word(word) for word in L]
	L += [shuffle_word(word) for word in L]
	print(L)
	L = sorted(L, key=cmp_to_key(less_than_character_count))
	print(L)

	oneToTwenty = [i for i in range(1,22)]
	for elem in oneToTwenty:
		print(elem)
		print(binary_search(oneToTwenty, elem, 0, len(oneToTwenty)))

	print("==================================================")

	import numpy as np 
	muHeight, sigmaHeight = 170, 10
	muWeight, sigmaWeight = 140, 30
	heights = np.random.normal(muHeight, sigmaHeight, 3)
	weights = np.random.normal(muWeight, sigmaWeight, 3)
	people = []
	for i in range(len(heights)):
		person = CircusPerson(heights[i], weights[i])
		people += [person]
	print([str(person) for person in people])
	people = sorted(people)
	print([str(person) for person in people])
	peopleGrouped = []
	currentGroup = []
	groupCount = 1
	for i in range(len(people)):
		if i == len(people) - 1:
			if len(currentGroup) > 0:
				peopleGrouped += [currentGroup + [people[-1]]]
			else:
				peopleGrouped += [[people[-1]]]
		else:
			if people[i] < people[i+1]:
				currentGroup += [people[i]]
				peopleGrouped += [currentGroup]
				currentGroup = []
				groupCount += 1
			else:
				currentGroup += [people[i]]

	print(len(peopleGrouped))
	print([[str(person) for person in group] for group in peopleGrouped])
	# for group in peopleGrouped:
	# 	print([str(person) for person in group])

if __name__ == "__main__":
	main()