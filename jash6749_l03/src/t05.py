"""
-------------------------------------------------------
Lab 3, pq_to_array
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Sngh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_pq, pq_to_array
from Queue_array import Queue
# Constants

pq = Queue()
source = [1, 2, 3, 4, 5]
array_to_pq(pq, source)

target = []
pq_to_array(pq, target)
print(target)
