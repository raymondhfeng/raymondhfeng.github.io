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
print(t1)

"""
		1
	  /	   \
	2		3
      \      \
      4	      7
      /     /
     8      9
"""

eight = Node(8)
four = Node(4,eight,None)
two = Node(2,None,four)
nine = Node(9)
seven = Node(7,nine,None)
three = Node(3,None,seven)
one = Node(1,two,three)
t2 = Tree(one)
t2.assignNbr()
print(t2)