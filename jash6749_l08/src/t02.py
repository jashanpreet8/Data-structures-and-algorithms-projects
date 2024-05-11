"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-03-07"
-------------------------------------------------------
"""
# Imports
from morse import fill_code_bst, decode_morse
from BST_linked import BST
# Constants
DATA1 = (('A', '.-'), ('B', '-...'), ('C', '-.-.'),
         ('D', '-..'), ('E', '.'), ('F', '..-.'),
         ('G', '--.'), ('H', '....'), ('I', '..'),
         ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'),
         ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
         ('S', '...'), ('T', '-'), ('U', '..-'),
         ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..'))

bst = BST()
fill_code_bst(bst, DATA1)
code = ''
print(decode_morse(bst, code))
