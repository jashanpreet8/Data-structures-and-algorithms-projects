"""
-------------------------------------------------------
Assignment 5, List_array
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-10"
-------------------------------------------------------
"""
# Imports
from List_array import List
from Food_utilities import read_foods
# Constants
"""
__eq__ 
__getitem__
append
clean
combine
intersection
prepend
remove_front
remove_many
split
split_alt
union"""

fh = open('foods.txt', 'r', encoding='utf-8')
foods = read_foods(fh)
fh.close()

l1 = List()
l2 = List()
vals = [1, 2, 3]
# for v in vals:
#    l1.append(v)

for food in foods:
    l1.append(food)

print(f"Equal: {l1 == l2}")

print(f"Get_item: {l1[1]}")

l1.append(2)
print(f"Append: {l1._values}")

l1.clean()
print(f"Clean: {l1._values}")

tar = List()
tar.combine(l1, l2)
print("Combine:", tar._values)

inter = List()
inter.intersection(l1, l2)
print("Intersection:", inter._values)

l1.prepend(0)
print("Prepend:", l1._values)

print("Remove_front:", l1.remove_front())

l1.remove_many(2)
print("Remove_many:", l1._values)

t1, t2 = l2.split()
print("Split:", t1._values, t2._values)

t1, t2 = l2.split_alt()
print("Split_alt:", t1._values, t2._values)

uni = List()
uni.union(l1, l2)
print("Union:", uni._values)
