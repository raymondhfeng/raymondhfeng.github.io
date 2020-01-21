from btree import Tree, Node

# 			1
# 		/		\
# 	2				3
#  /  \ 	      /   \
# 4		5		6		7

four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
three = Node(3, six, seven)
two = Node(2, four, five)
one = Node(1, two, three)
t1 = Tree(one)
t1.assignNbr()
t1.printLevelOrder()
print(t1.inOrderRecur())
print(t1.preOrderRecur())