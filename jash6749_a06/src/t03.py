"""
-------------------------------------------------------
Assignment 6, Task 3
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
# Constants

dq = Deque()
dq2 = Deque()
print("Empty before:", dq.is_empty())

dq.insert_front(2)
dq.insert_rear(1)
dq.insert_rear(3)
dq.insert_front(4)
dq.insert_front(0)

dq2.insert_rear(1)
dq2.insert_front(2)
print(dq == dq2)


curr = dq._front
while curr:
    print(curr._value)
    curr = curr._next

print("Len:", len(dq))

dq.remove_front()
dq.remove_rear()
dq.remove_front()
curr = dq._front
while curr:
    print(curr._value)
    curr = curr._next
print(dq.peek_front())
print(dq.peek_rear())


l = dq._front
r = dq._rear
dq._swap(l, r)
print("Swap")
curr = dq._front
while curr:
    print(curr._value)
    curr = curr._next
