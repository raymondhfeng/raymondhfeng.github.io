def arrayChanger(arr):
	arr[0] = 999

def main():
	arr = [0]
	arrayChanger(arr)
	print(arr)

if __name__ == "__main__":
	main()