from Stack import Stack
class Graph:
	# A 1 at index (a,b) means that there is a directed connection from a to b
	# An undirected graph will have a symmetric adjacency matrix
	# A directed graph has no such guarantees
	def __init__(self, num_nodes=0):
		self.adj = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
		for i in range(len(self.adj)):
			self.adj[i][i] = 1

	# Returns true if there is a path from a to b, or vice versa
	# Essentially does DFS from both nodes
	def connected(self, a, b): 
		def dfs(a):
			to_process = Stack()
			seen = set()
			to_process.push(a)
			while not to_process.empty():
				print("to_process: ", to_process)
				curr = to_process.pop()
				print("curr: ", curr)
				print("seen:", seen)
				if curr not in seen:
					seen.add(curr)	
					goes_to = self.adj[curr]
					for i in range(len(goes_to)):
						if goes_to[i] == 1 and i not in seen:
							to_process.push(i)
			return seen
		a_start = dfs(a)
		b_start = dfs(b)
		return a in b_start or b in a_start

	def add_d_conn(self, a, b):
		self.adj[a][b] = 1

	def add_conn(self, a, b):
		self.adj[a][b] = 1
		self.adj[b][a] = 1
