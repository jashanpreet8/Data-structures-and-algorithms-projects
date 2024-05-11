"""
-------------------------------------------------------
Assignment 3, Functions
-------------------------------------------------------
Author:  Jashanpreet Singh Jashanpreet Singh
ID:      169046749
Email:   jash6749@mylaurier.ca
__updated__ = "2024-02-05"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    while not source1.is_empty() or not source2.is_empty():
        if not source1.is_empty():
            target.push(source1.pop())
        if not source2.is_empty():
            target.push(source2.pop())

    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    array = []
    while not source.is_empty():
        top = source.pop()
        array.append(top)
    for a in array:
        source.push(a)

    return


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    stack = Stack()
    for c in string:
        if c.isalpha():
            stack.push(c.lower())

    reverse = ''
    while not stack.is_empty():
        reverse += stack.pop()

    filter = ''
    for c in string:
        if c.isalpha():
            filter += c.lower()

    return filter == reverse


# Constants
OPERATORS = "+-*/"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    elements = string.split(' ')
    for c in elements:
        if c.isdigit():
            stack.push(float(c))
        elif c in OPERATORS:
            operand1 = stack.pop()
            operand2 = stack.pop()

            if c == '+':
                result = operand2 + operand1
            elif c == '-':
                result = operand2 - operand1
            elif c == '*':
                result = operand2 * operand1
            else:
                if operand1 != 0:
                    result = operand2 / operand1

            stack.push(result)
    answer = stack.pop()

    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    """
    stack = Stack()
    path = []
    key = 'Start'
    while key != 'X':
        values = maze[key]
        if values:
            for i in range(len(values)):
                stack.push(values[i])
            key = stack.pop()
            path.append(key)
        else:
            if not stack.is_empty():
                key = stack.pop()
                path.append(key)
            else:
                key = 'X'
                path = None

    return path
    """
    path = []
    stack = Stack()
    loc = 'Start'
    while loc != 'X' and path is not None:
        for point in maze[loc]:
            if point not in path:
                stack.push(point)
        if not stack.is_empty():
            loc = stack.pop()
            path.append(loc)
        else:
            path = None
    return path
