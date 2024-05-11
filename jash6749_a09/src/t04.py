"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-03-23"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
# Constants

bst = BST()
vals = [1, 2, 3, 4, 5, 6]
for v in vals:
    bst.insert(v)

print("Contains")
print(f"{1 in bst}")
print(f"{3 in bst}")
print(f"{6 in bst}")
print(f"{5 in bst}")
print(f"{0 in bst}")
print("-"*25)

print("node count")
z, o, t = bst.node_counts()
print("Zero children:", z)
print("One children:", o)
print("Two children:", t)
print("-"*25)

print("parent")
key = 1
print(f"parent of {key}: {bst.parent(key)}")
print("-"*25)

print("parent_r")
key = 1
print(f"parent of {key}: {bst.parent_r(key)}")
