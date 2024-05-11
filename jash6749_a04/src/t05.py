"""
-------------------------------------------------------
Assignment 4, Task 5
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-07"
-------------------------------------------------------
"""
# Imports
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq
# Constants

pq = Priority_Queue()
lst = [22, 33, 11, 55, 44]
print("List: ", lst)
array_to_pq(pq, lst)
t1, t2 = pq_split_key(pq, 56)
print("Target1 (with higher priority):")
for v in t1:
    print(f"{v} ", end='')
print()
print("Target2 (with lower priority):")
for v in t2:
    print(f"{v} ", end='')
