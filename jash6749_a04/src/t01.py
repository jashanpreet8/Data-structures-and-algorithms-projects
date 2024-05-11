"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue
# Constants

cq, target = Queue(3), Queue(3)
lst = [1, 2, 3]
l2 = [3, 1, 2]

print(f"Empty before: {cq.is_empty()}")
print(f"Full before: {cq.is_full()}")
print(f"length before: {len(cq)}")
print(f"Equal before: {cq == target}")
print(f"List: {lst}")
for l in lst:
    cq.insert(l)
for l in l2:
    target.insert(l)
print("Inserting list:")
for v in cq:
    print(v)
print(f"Empty after: {cq.is_empty()}")
print(f"Full after: {cq.is_full()}")
print(f"length after: {len(cq)}")
target.remove()
print(f"Equal after: {cq == target}")
print(f"Peek: {cq.peek()}")
print("Removing list:")
for _ in range(len(cq)):
    print(cq.remove())
