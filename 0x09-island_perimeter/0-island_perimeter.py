#!/usr/bin/python3
"""Define island perimeter
"""


def island_perimeter(grid):
    """Computes perimeter of the grid
    """
    totPerim = 0
    connections = 0
    for row in grid:
        for col in row:
            if col == 1:
                totPerim += 4

    for row in range(len(grid)):
        for i in range(len(grid[row])):
            if grid[row][i] == 1:
                if grid[row][i-1] == 1:
                    connections += 2
                if grid[row - 1][i] == 1:
                    connections += 2

    return (totPerim - connections)
