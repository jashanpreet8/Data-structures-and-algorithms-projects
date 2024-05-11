"""
-------------------------------------------------------
Lab 4, Task 3
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-31"
-------------------------------------------------------
"""
# Imports
from utilities import list_test
from Food_utilities import read_foods
# Constants
fh = open('foods.txt', 'r', encoding='utf-8')
foods = read_foods(fh)
fh.close()

source = [1, 2, 3, 4, 5]
list_test(foods)
