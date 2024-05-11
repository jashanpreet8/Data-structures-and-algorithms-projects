"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-03-30"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque
from Sorts_Deque_linked import Sorts


arr = [
    44, 36, 10, 17, 7, 2, 98, 54, 97, 33,
    1, 11, 57, 2, 73, 69, 37, 29, 49
]


a = Deque()

for value in arr:
    a.insert_rear(value)

Sorts.gnome_sort(a)

for value in a:
    print(value, end=", ")
