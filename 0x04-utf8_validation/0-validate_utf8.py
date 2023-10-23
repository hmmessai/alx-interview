#!/usr/bin/python3
"""
Define method validUTF8
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determines if a given data set represents a valid
    utf-8 encoding
    """
    for no in data:
        binary = bin(no)
        for idx, x in enumerate(binary):
            if idx >= 2 and idx <= 6:
                if x == '0':
                    break
                if idx == 6:
                    if x == '1':
                        return False


        """if x == 0 and x == 1:
                continue
            if x != 6:
                if y == '1':
                    continue
                elif y == '0':
                    break
            if y == '1':
                return False
                """
    return True
