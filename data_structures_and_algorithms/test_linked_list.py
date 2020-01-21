from LinkedList import LinkedList, LLNode
import random

l = LinkedList(LLNode(0))
for _ in range(5):
    # l.append(random.randint(0, 100))
    l.append(3)

print(l)
l.removeDuplicatesTempBuffer()
print(l)

l2 = LinkedList(LLNode(0))
for _ in range(5):
    # l.append(random.randint(0, 100))
    l2.append(3)

print(l2)
l2.removeDuplicatesWithoutTempBuffer()
print(l2)