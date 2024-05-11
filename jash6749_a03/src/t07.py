"""
-------------------------------------------------------
Assignment 3, Task 7
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze
# Constants

maze1 = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
         'D': [], 'E': ['F', 'X'], 'F': ['G', 'H'], 'G': [], 'H': []}


maze2 = {'Start': ['A'], 'A': ['X', 'B'], 'B': ['A']}

maze3 = {'Start': ['A'], 'A': []}

maze4 = {'Start': ['A'], 'A': ['B', 'C'], 'B': [], 'C': ['D', 'E'],
         'D': [], 'E': ['X', 'F'], 'F': ['G'], 'G': ['C']}

print(stack_maze(maze4))
