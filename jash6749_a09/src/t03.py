"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-03-22"
-------------------------------------------------------
"""
# Imports
from functions import insert_words, comparison_total
from Hash_Set_BST import HS_BST
# Constants

print("Using linked BST Hash_Set")

fv = open("otoos610.txt", "r", encoding="utf-8")
hs = HS_BST(20)
insert_words(fv, hs)
fv.close()
total, word = comparison_total(hs)

print(f"Total Comparisons: {total:,}")
print(f"Word with maximum comparisons '{word.word}': {word.comparisons:,}")
