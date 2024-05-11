"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-03-09"
-------------------------------------------------------
"""
# Imports
from Sorted_List_linked import Sorted_List
# Constants
"""
__contains__
__eq__
__getitem__
_linear_search
clean
count
find
index
insert
intersection
max
min
peek
remove
remove_front
union"""

s, t1, t2 = Sorted_List(), Sorted_List(), Sorted_List()
t1.append(1)
t1.append(2)
t2.append(3)
t2.append(4)
print('combine')
s.combine(t1, t2)
curr = s._front
while curr:
    print(curr._value)
    curr = curr._next
