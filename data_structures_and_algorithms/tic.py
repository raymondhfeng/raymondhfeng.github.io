import fileinput

class tic:
	def __init__(self): #
		self.board = [['-']*3 for _ in range(3)]
		self.count = 0

	def __str__(self):
		result = ""
		for i in range(len(self.board)):
			for j in range(2):
				result += str(self.board[i][j])
				result += "|"
			result += str(self.board[i][2])
			result += "\n"
		return result

	def update(self, coord, player): #player 0 or 1. 
		if validate_input(coord):
			if player:
				self.board[coord[0]][coord[1]] = 'X'
			else:
				self.board[coord[0]][coord[1]] = 'O'
			self.count += 1

	def ai_move(self):
		if self.full():
			raise Exception("Board is full")
		else:
			for i in range(3):
				for j in range(3):
					if self.board[i][j] == '-':
						self.update((i,j),0)
						print("AI did move " + str(i) + "," + str(j))
						return

	def full(self):
		if self.count >= 9:
			return True

	def validate_input(self, coord):
		if coord[0] > 2 or coord[0] < 0 or coord[1] > 2 or coord[0] < 0:
			raise Exception()


def main():
	board = tic()
	print(board)

	# board.update((0,1),1)
	# print(board)

	# print(board.full())

	# for i in range(3):
	# 	for j in range(3):
	# 		# board.update((i,j), 1)
	# 		board.ai_move()
	# 		print(board)

	# print(board.full())

	# board.ai_move()

	# board.update((0,0), 1)
	# board.ai_move()
	# print(board)
	print("hi, let's play tic tac toe")
	print("enter your move line by line")
	for line in fileinput.input():
		coord = (int(line[0]),int(line[1]))

		try:
			board.update(coord,1)
		except:
			print("That was an invalid move, try again")

		try:
			board.ai_move()
		except:
			print("The game is over")
			break
		print(board)

if __name__ == "__main__":
	main()