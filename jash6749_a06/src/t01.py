"""
-------------------------------------------------------
Assignment 6, Task 1
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue
# Constants

qu = Queue()
qu2 = Queue()
tar = Queue()
lst = [1, 2, 3, 4]
print("Empty before:", qu.is_empty())
print('qu')
for l in lst:
    qu.insert(l)
current = qu._front
while current:
    print(current._value)
    current = current._next

print("Empty after:", qu.is_empty())
print("Len:", len(qu))
print("Remove:", qu.remove())
print("Peek:", qu.peek())
print("Equals:", qu == tar)
tar._move_front_to_rear(qu)
print('qu after')
current = qu._front
while current:
    print(current._value)
    current = current._next

print('tar')
current = tar._front
while current:
    print(current._value)
    current = current._next
tar._append_queue(qu)
tar.combine(qu, qu2)

t1, t2 = qu.split_alt()
print('t1')
current = t1._front
while current:
    print(current._value)
    current = current._next
print('t2')
current = t2._front
while current:
    print(current._value)
    current = current._next
print('qu after')
current = qu._front
while current:
    print(current._value)
    current = current._next
