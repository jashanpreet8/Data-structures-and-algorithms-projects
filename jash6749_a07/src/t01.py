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
from List_linked import List
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

self, target, comb = List(), List(), List()
self.append(1)
self.append(2)
target.append(3)
target.append(3)

print('eq')
print(self == target)

print('__getitem__')
print(target[0])

print('append')
print('working')

print('clean')
target.clean()
curr = target._front
while curr:
    print(curr._value)
    curr = curr._next

print('combine')
comb.combine(self, target)
curr = comb._front
while curr:
    print(curr._value)
    curr = curr._next

print('intersection')


print('prepend')


print('remove_front')


print('remove_many')


print('split')


print('split_alt')


print('union')
