"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Sngh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze
# Constants

fv = open('foods.txt', 'r', encoding='utf-8')
print(file_analyze(fv))
fv.close()
