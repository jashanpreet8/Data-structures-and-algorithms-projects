"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from functions import stack_reverse
# Constants

from Stack_array import Stack
from utilities import array_to_stack
# Constants

source = Stack()
array = [5, 8, 12]
array_to_stack(source, array)

print('Before:')
for a in source:
    print(a)
print()

stack_reverse(source)

print("After:")
for a in source:
    print(a)
