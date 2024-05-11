"""
-------------------------------------------------------
Lab 2, Task 5
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Sngh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-17"
-------------------------------------------------------
"""
# Imports
from utilities import stack_test
from Food_utilities import read_foods
# Constants

fh = open('foods.txt', 'r', encoding='utf-8')
foods = read_foods(fh)
fh.close()

stack_test(foods)
