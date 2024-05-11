"""
-------------------------------------------------------
Lab 7, Task 1
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-26"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

lst = List()
l = [1, 2, 3]
for v in l:
    lst.append(v)

p, c, i = lst._linear_search_r(0)
print(p)
print(c)
print(i)
