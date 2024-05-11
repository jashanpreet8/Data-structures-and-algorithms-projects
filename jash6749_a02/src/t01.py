"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Sngh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
from Food_utilities import by_origin, read_foods
# Constants

fh = open('foods.txt', 'r', encoding='utf-8')
foods = read_foods(fh)
fh.close()

origins = by_origin(foods, 11)
for o in origins:
    print(o)
