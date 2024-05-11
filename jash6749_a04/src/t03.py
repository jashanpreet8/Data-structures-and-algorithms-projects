"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from functions import queue_split_alt
from Queue_array import Queue
from utilities import array_to_queue
# Constants

q = Queue()
lst = [1]
print("List: ", lst)
array_to_queue(q, lst)
t1, t2 = queue_split_alt(q)
print("Target1:")
for v in t1:
    print(f"{v} ", end='')
print()
print("Target2:")
for v in t2:
    print(f"{v} ", end='')
