"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-03-15"
-------------------------------------------------------
"""
# Imports
from Letter import Letter
# Constants


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0
    for line in file_variable:
        for char in line:
            if char.isalpha():
                letter = Letter(char.upper())
                meter = bst.retrieve(letter)
                if meter.letter != char.upper():
                    print("Failure... ", meter)
    return


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    for value in bst.inorder():
        total += value.comparisons
    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    total_count = 0
    letter_counts = {}

    for letter in bst.inorder():
        total_count += letter.count
        letter_counts[letter.letter] = letter.count

    print("Letter Count/Percent Table")
    print(f"Total Count: {total_count:,}\n")
    print("Letter  Count       %")
    print("---------------------")

    for letter, count in sorted(letter_counts.items()):
        percent = (count / total_count) * 100
        print(f"{letter:>5}{count:>8,}{percent:>7.2f}%")
