#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heappush, heappop
import copy


def numToCoord(num, height, width):
    row = num // height
    col = num % width
    return (row, col)

def manhattanHeuristic(puzzle):
    cumSum = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            coord = numToCoord(puzzle[i][j], len(puzzle), len(puzzle[i]))
            cumSum += abs(coord[0] - i) + abs(coord[1] - j)
    return cumSum 

def isSolved(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != i*len(puzzle)+j:
                return False
    return True

def possibleMoves(puzzle):
	possMoves = []
	for i in range(len(puzzle)):
		for j in range(len(puzzle[i])):
			if puzzle[i][j] == 0:
				if i != 0:
					possMoves += ["up"]
				if i != len(puzzle) - 1:
					possMoves += ["down"]
				if j != 0:
					possMoves += ["left"]
				if j != len(puzzle[i]) - 1:
					possMoves += ["right"]
				return possMoves 
	return None

def swap(puzzle, i, j, k, l):
	puzzle = copy.deepcopy(puzzle)
	temp = puzzle[i][j]
	puzzle[i][j] = puzzle[k][l]
	puzzle[k][l] = temp
	return puzzle

def generateNeighbors(puzzle):
	print("the puzzle")
	print2d(puzzle)
	neighbors = []
	for i in range(len(puzzle)):
		for j in range(len(puzzle[i])):
			if puzzle[i][j] == 0:
				if i != 0:
					neighbors += [swap(puzzle,i,j,i-1,j)]
				if i != len(puzzle) - 1:
					neighbors += [swap(puzzle,i,j,i+1,j)]
				if j != 0:
					neighbors += [swap(puzzle,i,j,i,j-1)]
				if j != len(puzzle[i]) - 1:
					neighbors += [swap(puzzle,i,j,i,j+1)]
				for neighbor in neighbors:
					print2d(neighbor)
				return neighbors
	return None

def print2d(arr):
	for row in arr:
		print(row)
	print()
#
# Complete the 'movesToSolve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY puzzle as parameter.
#
def movesToSolve(puzzle):
	heapq = []
	heappush(heapq, (manhattanHeuristic(puzzle), 0, puzzle))
	alreadyVisited = []
	alreadyVisited += [puzzle]
	counter = 0
	while len(heapq) != 0:
		if counter > 10:
			return
		counter += 1
		currState = heappop(heapq)
		print(currState[1])
		# if currState[1] not in alreadyVisited:
		# 	alreadyVisited += [currState]
		if isSolved(currState[2]):
			print("SOLVED!")
			# print(currState)
			return currState[1]
		for elem in currState[2]:
			print(elem)
		print(manhattanHeuristic(currState[2]))
		print()
		neighbors = generateNeighbors(currState[2])
		for neighbor in neighbors:
			if neighbor not in alreadyVisited:
				alreadyVisited += [neighbor]
				# heappush(heapq, (manhattanHeuristic(neighbor)+currState[1]+1, currState[1]+1 ,neighbor))
				heappush(heapq, (manhattanHeuristic(neighbor), currState[1]+1 ,neighbor))



def main():
	# puzzle = [[1,6,3],[8,7,2],[4,0,5]]
	# print(possibleMoves(puzzle))
	# print(generateNeighbors(puzzle))
	# print(movesToSolve(puzzle))

	puzzle2 = [[0,4,2],[3,1,5],[6,7,8]]
	# print(movesToSolve(puzzle2))
	print2d(puzzle2)
	print(manhattanHeuristic(puzzle2))

	# puzzle3 = [[2,7,1],[6,3,5],[0,4,8]]
	# print(movesToSolve(puzzle3))

if __name__ == "__main__":
	main()

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     puzzle_rows = int(input().strip())
#     puzzle_columns = int(input().strip())

#     puzzle = []

#     for _ in range(puzzle_rows):
#         puzzle.append(list(map(int, input().rstrip().split())))

#     result = movesToSolve(puzzle)

#     fptr.write(str(result) + '\n')

#     fptr.close()
