"""
-------------------------------------------------------
Lab 1, Task 7
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods, get_vegetarian
# Constants

fr = open('foods.txt', 'r', encoding='utf-8')
foods = read_foods(fr)
fr.close()

vegs = get_vegetarian(foods)
for veg in vegs:
    print(veg)
    print()
