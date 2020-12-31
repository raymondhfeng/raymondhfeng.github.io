import math

# Write a function to determine the number of bits required to convert 
# integer A to integer B.
def bitSwapsAToB(A,B): # 
	xorResult = XOR(intToBitstring(A), intToBitstring(B))
	count = 0
	for elem in xorResult:
		if elem == "1":
			count += 1
	return count

def XOR(a,b): # returns the XOR of the bitstrings a and b
	minLength = min(len(a),len(b))
	maxLength = max(len(a),len(b))
	result = ""
	for i in range(minLength):
		if a[len(a) - i - 1] != b[len(b) - i - 1]:
			result = "1" + result
		else:
			result = "0" + result
	for i in range(maxLength - minLength):
		if len(a) > len(b):
			result = a[i] + result
		elif len(b) > len(a):
			result = b[i] + result
	return result

def intToBitstring(n): #turns the base 10 number n into a bitstring
	if n == 0:
		return "0"
	else:
		currPow = 0
		while math.pow(2,currPow+1) <= n:
			currPow += 1
		result = ""
		while currPow >= 0:
			powVal = math.pow(2,currPow)
			if powVal <= n:
				result += "1"
				n -= powVal
			else:
				result += "0"
			currPow -= 1
		return result

# You are given two 32-bit numbers, N and M, and two bit positions, i and j. 
# Write a method to insert M into N such that M starts at bit j and ends at bit i. 
# You can assume that the bits j through i have enough space to fit all of M. 
# That is, if M=10011, you can assume that there are at least 5 bits between j and i. 
# You would not, for example, have j=3 and i=2, because M could not fully fit between
# bit 3 and bit 2.
def insertBitsAt(N,M,i,j):
	print(bin(N))
	print(bin(M))

# Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double, 
# print the binary representation. If the number cannot be represented accurately 
# in binary with at most 32 characters, print “Error”.
def doubleToBinary(dubb):
	if dubb >= 1 or dubb <= 0:
		return -1
	else:
		result = ""
		currVal = dubb
		for i in range(32):
			currVal = currVal * 2
			# print(currVal)
			if currVal >= 1:
				currVal -= 1
				result = result + "1"
			else:
				result = result + "0"
		if currVal != 0:
			return -1
		return result



def main():
	for i in range(10):
		print("The base 10 number " + str(i) + " in binary is: " + intToBitstring(i))

	# print(XOR("1","01"))
	print(bitSwapsAToB(1,2))
	print(bitSwapsAToB(64,2))
	print(bitSwapsAToB(4,2))
	print(bitSwapsAToB(0,0))
	print(bitSwapsAToB(8,8))

	print("what in the balls")
	print(bin(~0))
	print(bin(55 | 1))
	print(bin(99))
	print(bin(99 << 5))
	print(insertBitsAt(3452,49,1,4))

	print(bin(99))
	for elem in bin(99):
		print(elem)

	# print(doubleToBinary(0.5))
	# print(doubleToBinary(0.75))
	print(doubleToBinary(0.8))
	print(doubleToBinary(0.875))

	for elem in bin(63):
		print(elem)

if __name__ == "__main__":
	main()


