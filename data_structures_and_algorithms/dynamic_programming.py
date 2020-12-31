# A child is running up a staircase with n steps, and can hop either 
# 1 step, 2 steps, or 3 steps at a time. Implement a method to count 
# how many possible ways the child can run up the stairs.

# Define subproblem: F(n) := the number of ways that the baby can reach the end starting n steps from the finish
# Base cases: F(0)=0, F(1)=1, F(2)=2, F(3)=4
# Recurrence: F(n)=F(n-1)+F(n-2)+F(n-3)
# We have three options, hopping one, two, or three steps. Summing those three options gives us our total number of options.  

def baby_upstairs(n=100):
	result = [0]*n
	result[0] = 0
	result[1] = 1
	result[2] = 2
	result[3] = 3
	for i in range(4,n):
		result[i] = result[i-1]+result[i-2]+result[i-3]
	print(result[n-1])

# Imagine a robot sitting on the upper left corner of an X by Y grid. 
# The robot can only move in two directions: right and down. 
# How many possible paths are there for the robot to go from (0,0) to (X,Y)? Follow up: 
# Imagine certain spots are "off limits", such that the robot cannot step on them. 
# Design an algorithm to find a path for the robot from the top left to the bottom right.
# Setup: nxn grid, start from top left, end at bottom right
# Subproblem: F(a,b), the number of ways to get to the goal starting from coordinates (a,b)
# Base cases: F(n-1,n-1) = 1. Once you're at the goal, only one way to get to the goal. 
# Recurrence, build leftwards and upwards.
# Forbidden set extension should be relatively easy. Non-forbidden set should just be binomial coefficients.
def robot_in_grid(n=5,forbidden=[]):
	result = [[0]*n for _ in range(n)]
	result[n-1][n-1] = 1
	for i in range(1,n):
		currIndex = n-i-1
		result[currIndex][n-1] = 1
		result[n-1][currIndex] = 1
	for i in range(1,n):
		currIndex = n-i-1
		result[currIndex][currIndex] = result[currIndex+1][currIndex] + result[currIndex][currIndex+1]
		for j in range(i,n):
			jIndex = n-j-1
			result[currIndex][jIndex] = result[currIndex+1][jIndex] + result[currIndex][jIndex+1]
			result[jIndex][currIndex] = result[jIndex+1][currIndex] + result[jIndex][currIndex+1]
	return result 

# def magic_index(A): # finds magic index in A, if it exists. Assumes all elements distinct.
# 	def helper(A, lower, upper):
		

def all_subsets(S): # returns all subsets of S
	def helper(arr):
		if len(arr) == 1:
			return [arr]
		else:
			result = []
			subsets = helper(arr[1:])
			for elem in subsets:
				result += [[arr[0]] + elem]
				result += [elem]

			return result + [[arr[0]]]

	return helper(S) + [[]]


def all_permutations(S): # returns all permutations of string S
	def helper(arr):
		if len(arr) == 1:
			return [arr]
		else:
			sub = helper(arr[1:])
			result = []
			for elem in sub:
				for i in range(len(elem)+1):
					insertedAtI = elem[:i] + [arr[0]] + elem[i:]
					result += [insertedAtI]
			return result
	perms = helper(S)
	perms = ["".join(elem) for elem in perms]
	return perms

import random

def random_array(n): # generates a random shuffle of the integers from 0 to n-1
	arr = [i for i in range(n)]
	def swapFirst(arr):
		index = random.randint(1,len(arr)-1)
		print(index)
		temp = arr[0]
		arr[0] = arr[index]
		arr[index] = temp
		return arr
	def helper(arr):
		if len(arr) == 1:
			return arr
		else:
			arr = [arr[0]] + helper(arr[1:])
			arr = swapFirst(arr)
			return arr
	return helper(arr)

# the number of ways that we can divide n into k partitions
# partitions must have nonzero size
# returns all the partitions as a list of lists
# def partition(n,k): 
# 	if n == 0:
# 		return [[]]
# 	if k == 1:
# 		return [[n]]
# 	result = []
# 	for i in range(1,n):
# 		subresult = partition(n-i, k-1)
# 		for part in subresult:
# 			result += [[i] + part]
# 	return result

# # given a list of lists, returns the cartesian sum
# def cartesianSum(arr): 
# 	curr = arr
# 	while len(curr) > 1:
# 		cart1 = curr[0]
# 		cart2 = curr[1]
# 		cartHolder = []
# 		for i in range(len(cart1)):
# 			for j in range(len(cart2)):
# 				cartHolder += [cart1[i] + cart2[j]]
# 		curr = [cartHolder] + curr[2:]
# 	return curr

# def npairs(n):
# 	pairCache = {}
# 	def helper(n):
# 		if n == 1:
# 			return ["()"]
# 		result = []
# 		for i in range(2, n+1):
# 			partitionings = partition(n,i)
# 			for part in partitionings:
# 				toCartSum = []
# 				for num in part:
# 					print("toCartSum")
# 					print(toCartSum)
# 					print("partitionings")
# 					print(partitionings)
# 					if num in pairCache:
# 						toCartSum += [pairCache[num]]
# 					else:
# 						numRes = helper(num)
# 						toCartSum += [numRes]
# 						pairCache[num] = numRes			
# 				result += cartesianSum(toCartSum)[0]
# 			print("result")
# 			print(result)		
# 			# print("result")
# 			# print(result)
# 			# print("cartesian sum")
# 			# print(cartesianSum(toCartSum))
# 		# print("n")
# 		# print(n)
# 		# print("toCartSum")
# 		# print(toCartSum)
# 		print(pairCache)
# 		return result + [onePartition(n)]
# 	return helper(n)

# def onePartition(n): # Returns the special case of one partition of n parenthesis
# 	toReturn = ""
# 	for i in range(n):
# 		toReturn = "(" + toReturn
# 		toReturn = toReturn + ")"
# 	return toReturn

def cartesianSum(arr1,arr2):
	result = []
	for i in range(len(arr1)):
		for j in range(len(arr2)):
			result += [arr1[i]+arr2[j]]
	return result

# second attempt for npairs
def npairs(n):
	if n == 0:
		return []
	elif n == 1:
		return ["()"]
	else:
		result = []
		for i in range(1,n):
			print("i")
			print(i)
			print("n-i")
			print(n-i)
			cart1 = npairs(i)
			cart2 = npairs(n-i)
			cartSum = cartesianSum(cart1,cart2)
			for elem in cartSum:
				if elem not in result:
					result += [elem]
		# print("cart1")
		# print(cart1)
		# print("cart2")
		# print(cart2)
		minus1 = npairs(n-1)
		for case in minus1:
			toInsert = ["(" + case + ")"]
			if toInsert not in result:
				result += toInsert
		return result

def changeCount(n):
	changeDict = {0:25,1:10,2:5,3:1}
	# the number of ways you can make n cents w/ a restricted set
	# k=0 -> quarters, etc. 
	def helper(n,k):
		if n == 0:
			return 1
		elif k == 3:
			return 1
		else:
			maxPoss = n // changeDict[k]
			total = 0
			for i in range(0, maxPoss+1):
				total += helper(n - changeDict[k]*i,k+1)
			return total
	return helper(n,0)

def main():
	# print(baby_upstairs(100))
	# result = robot_in_grid(4)
	# for elem in result:
	# 	print(elem)

	# print(random_array(10))

	# print(all_subsets([1,2,3]))
	# perms = all_permutations(list("ray"))
	# print(perms)
	# print(len(perms))

	# print(partition(2,2))

	# print(onePartition(3))

	# print(npairs(3))

	# print(npairs(2))

	# print(npairs(4))
	# print(len(npairs(4)))

	for i in range(1,11):
		print("cents:")
		print(i)
		print("numways:")
		print(changeCount(i))

if __name__ == "__main__":
	main()