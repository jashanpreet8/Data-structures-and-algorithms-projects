"""
-------------------------------------------------------
Lab 1, Task 5
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
# Constants

fh = open('foods.txt', 'r', encoding='utf-8')
lines = read_foods(fh)
fh.close()

for line in lines:
    print(line)
    print()
