"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack
# Constants

source = Stack()
array = [1, 2, 3]
array_to_stack(source, array)

print('Before:')
for a in source:
    print(a)
print()

source.reverse()

print("After:")
for a in source:
    print(a)
