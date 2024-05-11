"""
-------------------------------------------------------
Lab 2, Task 2
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Sngh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-29"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_stack
from Stack_array import Stack
# Constants

stack = Stack()
source = [5, 8, 12, 8]

array_to_stack(stack, source)

for v in stack:
    print(v)
