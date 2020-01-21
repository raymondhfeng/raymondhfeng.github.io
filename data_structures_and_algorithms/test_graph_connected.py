from graph import Graph

g = Graph(6)

g.add_conn(0,1)
g.add_conn(1,2)
g.add_conn(2,0)

g.add_conn(3,4)
g.add_conn(4,5)
g.add_conn(5,3)

print(g.connected(0,2))
print(g.connected(3,0))