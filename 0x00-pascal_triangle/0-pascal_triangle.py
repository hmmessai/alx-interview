#!/usr/bin/python3
"""
Defines pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n
    """
    if n <= 0:
        return []

    outer_list = []
    for n in range(n):
        inner_list = []
        for k in range(n + 1):
            try:
                inner_list.append(
                        int((factorial(n))/(factorial(k) * factorial(n - k))))
            except ZeroDivisionError:
                inner_list.append(1)
        outer_list.append(inner_list)
    return outer_list


def factorial(n):
    """
    Computes the factorial of a given number n
    """
    if n <= 1:
        return 1

    return n * factorial(n - 1)
