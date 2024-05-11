"""
-------------------------------------------------------
Lab 7, Task 3
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-27"
-------------------------------------------------------
"""
# Imports
from List_linked import List
# Constants

s = List()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
curr = s._front
while curr:
    print(curr._value)
    curr = curr._next
t1, t2 = s.split_alt_r()
