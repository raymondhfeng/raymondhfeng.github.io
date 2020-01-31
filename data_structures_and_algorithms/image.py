import random

class Image:
	def __init__(self, initial=None, size=10, rand=False): 
	#initial is the initial 2d array that represents the image, default is all zeroes
	#default size is 10x10
	#rand is only possibly non-None if initial is None
		if initial:
			self.img = initial
		else:
			if rand:
				self.img = [[0]*size for _ in range(size)]
				for i in range(len(self.img)):
					for j in range(len(self.img[i])):
						self.img[i][j] = random.randint(0, 9)
			else:
				self.img = [[0]*size for _ in range(size)]

	def __str__(self):
		result = ""
		for i in range(len(self.img)):
			result += str(self.img[i])
			result += '\n'
		return result

	# any columns and rows containing a zero will get zeroed out
	def zero_out(self): 
		rows = set()
		columns = set()
		for i in range(len(self.img)):
			for j in range(len(self.img[i])):
				if self.img[i][j] == 0:
					rows.add(i)
					columns.add(j)
		for i in rows:
			for k in range(len(self.img[i])):
				self.img[i][k] = 0
		for j in columns:
			for k in range(len(self.img)):
				self.img[k][j] = 0

	def rotate(self): #rotates the image clockwise by 90 degrees
		numRings = len(self.img) // 2
		for i in range(numRings):
			for j in range(i+1,len(self.img)-i):
				t1,t2 = (i,j)
				r1,r2 = (j,len(self.img)-1-i)
				b1,b2 = (len(self.img)-1-i,len(self.img)-1-j)
				l1,l2 = (len(self.img)-1-j,i)
				temp = self.img[t1][t2]
				self.img[t1][t2] = self.img[l1][l2]
				self.img[l1][l2] = self.img[b1][b2]
				self.img[b1][b2] = self.img[r1][r2]
				self.img[r1][r2] = temp

	def reflectMainDiagonal(self): 
		for i in range(len(self.img)):
			for j in range(i):
				temp = self.img[i][j]
				self.img[i][j] = self.img[j][i]
				self.img[j][i] = temp

	def reflectSecondaryDiagonal(self):
		for i in range(len(self.img)):
			for j in range(len(self.img) - i):
				temp = self[i][j]
				self[i][j] = self[len(self.img) - j][len(self.img) - i]
				self[len(self.img) - j][len(self.img) - i] = temp

def main():
	img = Image(None, 4, True)
	print(img)

	img.zero_out()
	print(img)

	img2 = Image([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
	print(img2)
	img2.rotate()
	print(img2)

if __name__ == "__main__":
	main()