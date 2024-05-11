"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2024-03-20"
-------------------------------------------------------
"""
# Imports
import random
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
        from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = []
    for value in range(SIZE):
        values.append(Number(value))

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
        from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values = []
    for value in range(SIZE-1, -1, -1):
        values.append(Number(value))

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    # your code here
    arrays = []
    for _ in range(TESTS):
        row = []
        for _ in range(SIZE):
            value = Number(random.randint(0, XRANGE))
            row.append(value)
        arrays.append(row)

    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    v1 = create_sorted()
    Number.comparisons = 0
    Sorts.swaps = 0
    func(v1)
    comp1 = Number.comparisons
    swap1 = round(Sorts.swaps)

    v2 = create_reversed()
    Number.comparisons = 0
    Sorts.swaps = 0
    func(v2)
    comp2 = Number.comparisons
    swap2 = round(Sorts.swaps)

    v3 = create_randoms()
    Number.comparisons = 0
    Sorts.swaps = 0
    func(v3)
    comp3 = Number.comparisons
    swap3 = round(Sorts.swaps)

    print(f"{title:<14} {comp1:>8} {comp2:>8} {comp3:>8} {swap1:>8} {swap2:>8} {swap3:>8}")

    return
