"""
-------------------------------------------------------
Assignment 5, Sorted_List_array
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-10"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
# Constants

"""
__contains__: you may not use the Python in operator
__eq__
__getitem__
clean
count: you may not use the Python count method
? find
index
intersection
max: you may not use the Python max method
min: you may not use the Python min method
peek
remove
remove_front
remove_many
split
split_alt
split_key
union
"""

l1 = Sorted_List()
l2 = Sorted_List()
vals = [1, 2, 3]
for v in vals:
    l1._values.append(v)

b = 4 in l1
print("Contains:", b)

print("Equal:", l1 == l2)

print("Get_item:", l1[1])

l2.clean()
print("Clean:", l2._values)

print("Count:", l1.count(1))

print("Find:", l1.find(2))

print("Index:", l1.index(5))

l2._values.append(3)
inter = Sorted_List()
inter.intersection(l1, l2)
print("Intersection:", inter._values)

print("Max:", l1.max())

print("Min:", l1.min())

print("Peek:", l1.peek())

print("Remove:", l2.remove(3))

print("Remove_front:", l1.remove_front())

l1.remove_many(2)
print("Remove_many:", l1._values)

for v in vals:
    l2._values.append(v)

t1, t2 = l2.split()
print("Split:", t1._values, t2._values)

t1, t2 = l2.split_alt()
print("Split_alt:", t1._values, t2._values)

t1, t2 = l1.split_key(2)
print("Split_key:", t1._values, t2._values)

for v in vals:
    l2._values.append(v)

uni = Sorted_List()
uni.union(l1, l2)
print("Union:", uni._values)
