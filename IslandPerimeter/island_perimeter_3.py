"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""

from typing import List, Dict


class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        lands = 0
        neighbours = 0
        rows = len(grid)
        cols = len(grid[0])

        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if grid[i][j] == 1:
                    lands += 1
                    if i >= 0 and j < cols - 1 and grid[i][j + 1] == 1:
                        neighbours += 1
                    if i < rows - 1 and j >= 0 and grid[i + 1][j] == 1:
                        neighbours += 1
        return 4 * lands - 2 * neighbours


def test_8():
    grid = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,1],
        [1,1,0,0]
    ]
    expected_result = 20
    s = Solution()
    res = s.islandPerimeter(grid)
    assert res == expected_result

def test_4():
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]
    expected_result = 6
    s = Solution()
    res = s.islandPerimeter(grid)
    assert res == expected_result


def test_7():
    grid = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]
    expected_result = 16
    s = Solution()
    res = s.islandPerimeter(grid)
    assert res == expected_result


def test_6():
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    expected_result = 16
    s = Solution()
    res = s.islandPerimeter(grid)
    assert res == expected_result


def test_5():
    grid = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0],
    ]
    expected_result = 8
    s = Solution()
    res = s.islandPerimeter(grid)
    assert res == expected_result





def test_3():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    expected_result = 4
    s = Solution()
    res = s.islandPerimeter(grid)
    assert res == expected_result


def test_2():
    grid = [[0, 1, 0]]
    expected_result = 4
    s = Solution()
    res = s.islandPerimeter(grid)
    assert res == expected_result


def test_1():
    grid = [[1]]
    expected_result = 4
    s = Solution()
    res = s.islandPerimeter(grid)
    assert res == expected_result


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
