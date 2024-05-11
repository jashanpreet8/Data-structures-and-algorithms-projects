"""
-------------------------------------------------------
Lab 4, Task 1
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-31"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_list
from List_array import List
# Constants

llist = List()
source = [1, 2, 3, 4, 5]
array_to_list(llist, source)
for i in range(len(llist)):
    print(llist[i])
