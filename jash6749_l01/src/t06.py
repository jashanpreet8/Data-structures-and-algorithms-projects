"""
-------------------------------------------------------
Lab 1, Task 6
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods, write_foods
# Constants

fr = open('foods.txt', 'r', encoding='utf-8')
fw = open('new_foods.txt', 'w', encoding='utf-8')

foods = read_foods(fr)
write_foods(fw, foods)

fr.close()
fw.close()
