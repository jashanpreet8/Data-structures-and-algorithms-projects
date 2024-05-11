"""
-------------------------------------------------------
Lab 7, Task 4
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

s1, s2, tar = List(), List(), List()
s1.append(1)
s1.append(2)
s2.append(1)
s2.append(3)

tar.intersection_r(s1, s2)
curr = tar._front
while curr:
    print(curr._value)
    curr = curr._next
