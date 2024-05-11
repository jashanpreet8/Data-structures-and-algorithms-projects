"""
-------------------------------------------------------
Tests various linked sorting functions.
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

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

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
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for value in range(SIZE):
        values.append(Number(value))

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
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
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    # your code here
    lists = List()
    for _ in range(TESTS):
        rows = List()
        for _ in range(SIZE):
            value = Number(random.randint(0, XRANGE))
            rows.append(value)
        lists.append(rows)

    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
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
    for lst in v3:
        func(lst)
    comp3 = Number.comparisons
    swap3 = round(Sorts.swaps)

    print(f"{title:<14} {comp1:>8} {comp2:>8} {comp3:>8} {swap1:>8} {swap2:>8} {swap3:>8}")

    return
