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


def main():
	print(baby_upstairs(100))
	result = robot_in_grid(4)
	for elem in result:
		print(elem)

if __name__ == "__main__":
	main()