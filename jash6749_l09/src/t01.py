"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-03-12"
-------------------------------------------------------
"""
# Imports
from functions import hash_table
from Food_utilities import read_foods
# Constants

fh = open('foods.txt', 'r', encoding='utf-8')
foods = read_foods(fh)
fh.close()

hash_table(7, foods)
