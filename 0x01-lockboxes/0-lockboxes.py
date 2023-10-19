#!/usr/bin/python3
"""
Defines canUnlockAll function
"""


"""def canUnlockAll(boxes):
    
    Determines if all the boxes can be opened
    Attributes:
        boxes(list of lists): contains all the boxes
    Return:
        True: if all boxes can be opened.
        False: otherwise.
    """

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True

    def dfs(box):
        unlocked[box] = True
        for key in boxes[box]:
            if not unlocked[key]:
                dfs(key)

    dfs(0)
    return all(unlocked)



