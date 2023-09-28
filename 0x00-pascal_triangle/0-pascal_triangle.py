#!/usr/bin/python3
"""
Defines pascal_triangle
"""
from math import factorial


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n
    """
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
