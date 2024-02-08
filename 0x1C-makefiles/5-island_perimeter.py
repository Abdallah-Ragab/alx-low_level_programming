#!/usr/bin/python3
"""Module that calculates the perimeter of an island in a grid."""


# def num_water_neighbors(grid, i, j):
#     """Returns the number of water neighbors a cell has in a grid."""

#     num = 0

#     if i <= 0 or not grid[i - 1][j]:
#         num += 1
#     if j <= 0 or not grid[i][j - 1]:
#         num += 1
#     if j >= len(grid[i]) - 1 or not grid[i][j + 1]:
#         num += 1
#     if i >= len(grid) - 1 or not grid[i + 1][j]:
#         num += 1

#     return num


# def island_perimeter(grid):
#     """Returns the perimeter of the island in grid."""

#     perim = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j]:
#                 perim += num_water_neighbors(grid, i, j)

#     return perim


def island_perimeter(grid):
    """
    Calculates the perimeter of an island represented by a grid.

    Args:
        grid (list): A 2D grid representing the island,
        where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    def cell_borders(grid, x, y):
        cell_top = grid[y - 1][x] if y > 0 else 0
        cell_bottom = grid[y + 1][x] if y < len(grid) - 1 else 0
        cell_left = grid[y][x - 1] if x > 0 else 0
        cell_right = grid[y][x + 1] if x < len(grid[y]) - 1 else 0

        return (cell_top, cell_bottom, cell_left, cell_right)

    def calculate_cell_perimeter(cell_borders):
        perimeter = 0
        for border in cell_borders:
            if border == 0:
                perimeter += 1
        return perimeter

    total_perimeter = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                total_perimeter += calculate_cell_perimeter(
                    cell_borders(grid, x, y)
                    )

    return total_perimeter
