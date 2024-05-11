"""
-------------------------------------------------------
Lab 3, priority_queue_test
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Sngh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-25"
-------------------------------------------------------
"""
# Imports
from utilities import priority_queue_test
from Food_utilities import read_foods
# Constants

fh = open('foods.txt', 'r', encoding='utf-8')
foods = read_foods(fh)
fh.close()

priority_queue_test(foods)
