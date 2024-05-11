"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Sngh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-18"
-------------------------------------------------------
"""
# Imports
from Food_utilities import food_search, read_foods
# Constants

fh = open('foods.txt', 'r', encoding='utf-8')
foods = read_foods(fh)
fh.close()

results = food_search(foods, -1, 100, False)
for r in results:
    print(r)
