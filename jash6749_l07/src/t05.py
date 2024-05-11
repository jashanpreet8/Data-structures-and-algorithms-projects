"""
-------------------------------------------------------
Lab 7, Task 5
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

tar, s1, s2 = List(), List(), List()
s1.append(22)
s1.append(33)
s1.append(11)
s1.append(55)
s2.append(11)
s2.append(55)
s2.append(44)
tar.union_r(s1, s2)

curr = tar._front
while curr:
    print(curr._value)
    curr = curr._next
