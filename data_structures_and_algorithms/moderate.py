def swap(): # swaps two elements in place without using a temprorary variable
	a = 10
	b = 15
	a = a+b
	b = a-b
	a = a-b

def countZeroes(n): # computes the number of trailing zeros in n factorial
	currPower = 1
	counter = 0
	while pow(5,currPower) <= n:
		multiple = 1
		while multiple*pow(5,currPower) <= n:
			counter += 1
			multiple += 1
		currPower += 1
	return counter

def allPairs(arr,n):
	numToIndex = {}
	for i in range(len(arr)):
		if arr[i] in numToIndex:
			numToIndex[arr[i]] += [i]
		else:
			numToIndex[arr[i]] = [i]
	print(numToIndex)
	result = []
	for i in range(len(arr)):
		if n - arr[i] in numToIndex:
			for index in numToIndex[n - arr[i]]:
				if index != i:
					result += [(i,index)]
	return result

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    currMax = -1 * sys.maxint
    runningSum = 0
    for i in range(len(nums)):
        if nums[i] >= 0:
            runningSum += nums[i]
            if runningSum > currMax:
                currMax = runningSum
        else:
            if currMax < 0 and nums[i] > currMax:
                currMax = nums[i]
            elif runningSum + nums[i] < 0:
                runningSum = 0
            else:
                runningSum += nums[i]
    return currMax

def main():
	arr = [1,2,3,4,5,6,7,8,9,10]
	print(allPairs(arr,10))

if __name__ == "__main__":
	main()