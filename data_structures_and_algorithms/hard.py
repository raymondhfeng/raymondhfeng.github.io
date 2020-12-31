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

# def random_m_from_arr(arr, m): # generates a random selection of m elements from an array of n. 

def main():
	print(random_array(10))


if __name__ == "__main__":
	main()