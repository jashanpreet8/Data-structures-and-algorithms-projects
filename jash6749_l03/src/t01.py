"""
-------------------------------------------------------
Lab 3, array_to_queue
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Sngh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_queue
from Queue_array import Queue
# Constants

queue = Queue()
source = [1, 2, 3, 4, 5]
array_to_queue(queue, source)

for value in queue:
    print(value)
