"""
-------------------------------------------------------
Assignment 4, Task 2
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

source, target = Queue(), Queue()
list1 = [1, 2, 3]
list2 = [1, 2, 3]
array_to_queue(source, list1)
array_to_queue(target, list2)

print(source == target)
