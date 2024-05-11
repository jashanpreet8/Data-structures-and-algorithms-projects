"""
-------------------------------------------------------
Assignment 3, Task 1
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
# Imports
from functions import stack_combine
from Stack_array import Stack
from utilities import array_to_stack
# Constants

source1, source2 = Stack(), Stack()
array1 = [5, 8, 12, 8]
array2 = [3, 6, 1, 7, 9, 14]
array_to_stack(source1, array1)
array_to_stack(source2, array2)

target = stack_combine(source1, source2)
for v in target:
    print(v)
