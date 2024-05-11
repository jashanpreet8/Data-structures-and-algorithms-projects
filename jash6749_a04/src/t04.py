"""
-------------------------------------------------------
Assignment 4, Task 4
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from utilities import array_to_queue
# Constants

q = Queue()
lst = [1]
print("List: ", lst)
array_to_queue(q, lst)
t1, t2 = q.split_alt()
print("Target1:")
for v in t1:
    print(f"{v} ", end='')
print()
print("Target2:")
for v in t2:
    print(f"{v} ", end='')
