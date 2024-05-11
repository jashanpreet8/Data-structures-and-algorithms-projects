"""
-------------------------------------------------------
Lab 6, Task 6
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-16"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

ll = List()
lst = [22, 33, 11, 55, 44]

for v in lst:
    ll.append(v)

ll[-1] = 99

current = ll._front
while current is not None:
    print(current._value)
    current = current._next
