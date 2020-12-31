def binary_search(arr,target):
	def helper(arr,target,i,j):
		splitIndex = (i + j) // 2
		splitKey = arr[splitIndex]
		if i >= j and target != splitKey:
			return -1
		elif target == splitKey:
			return splitIndex
		elif splitKey < target:
			return helper(arr,target,splitIndex+1,j)
		else:
			return helper(arr,target,i,splitIndex-1)
	return helper(arr,target,0,len(arr)-1)

def accessRotated(arr,i,k):
	return arr[(i+k)%len(arr)]

def rotated_binary_search(arr,target):
	rotation_index = 0
	for i in range(len(arr)-1):
		if arr[i + 1] < arr[i]:
			rotation_index = i+1
			break
	def helper(arr,target,i,j):
		splitIndex = (i + j) // 2
		splitKey = accessRotated(arr,splitIndex,rotation_index)
		if i >= j and target != splitKey:
			return -1
		elif target == splitKey:
			return (splitIndex + rotation_index) % len(arr)
		elif splitKey < target:
			return helper(arr,target,splitIndex+1,j)
		else:
			return helper(arr,target,i,splitIndex-1)
	return helper(arr,target,0,len(arr)-1)

def main():
	# arr = [elem for elem in range(8)]
	# for i in range(9):
	# 	print(binary_search(arr,i))

	# print("HOOPLA")

	# rotated = [4,5,6,7,0,1,2]
	# for i in range(8):
	# 	print(rotated_binary_search(rotated,i))

	print(rotated_binary_search([1,3,5],5))
	print(binary_search([1,3,5],5))
	print(binary_search([3,5,1],5))

if __name__ == "__main__":
	main()