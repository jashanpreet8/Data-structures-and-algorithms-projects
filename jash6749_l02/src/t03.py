"""
-------------------------------------------------------
Lab 2, Task 3
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Sngh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_stack, stack_to_array
from Stack_array import Stack
# Constants

stack = Stack()

source = [1, 2, 3, 4, 5]
array_to_stack(stack, source)

target = []
stack_to_array(stack, target)

print(target)
