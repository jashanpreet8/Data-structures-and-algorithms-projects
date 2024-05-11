"""
-------------------------------------------------------
Assignment 6, Task 2
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_linked import Priority_Queue
# Constants

pq = Priority_Queue()
pq2 = Priority_Queue()
tar = Priority_Queue()
print('Empty before:', pq.is_empty())
lst = [1, 2, 3, 4, 5]
for l in lst:
    pq.insert(l)
print("pq")
curr = pq._front
while curr:
    print(curr._value)
    curr = curr._next

print('Empty after:', pq.is_empty())
print('Len:', len(pq))
pq.remove()
print("Peek:", pq.peek())
t1, t2 = pq.split_alt()
t1, t2 = pq.split_key(0)
print("t1")
curr = t1._front
while curr:
    print(curr._value)
    curr = curr._next
print("t2")
curr = t2._front
while curr:
    print(curr._value)
    curr = curr._next
lst = [4, 5, 6]
for l in lst:
    pq2.insert(l)
print("pq2")
curr = pq2._front
while curr:
    print(curr._value)
    curr = curr._next

tar.combine(pq, pq2)

print("tar")
curr = tar._front
while curr:
    print(curr._value)
    curr = curr._next
