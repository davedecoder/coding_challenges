"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""

from typing import List, Dict


class Solution:

    def __init__(self):
        self.grid = [[]]
        self.mapped_land = {}
        self.perimeter = 0

    def is_land(self, x: int, y: int) -> bool:
        return self.grid[x][y] == 1

    def is_mapped(self, x: int, y: int) -> bool:
        return self.mapped_land.get(f"{x},{y}", False)

    def map_land(self, x: int, y: int):
        self.mapped_land[f"{x},{y}"] = True

    def is_offset(self, x: int, y: int) -> bool:
        if x < 0:
            return True
        if x >= len(self.grid):
            return True
        if y < 0:
            return True
        if y >= len(self.grid[0]):
            return True
        return False

    def next_neightbour(self, x: int, y: int) -> (int, int):
        yield x + 1, y
        yield x, y + 1
        yield x - 1, y
        yield x, y - 1

    def find_land(self, x: int, y: int, visited=None) -> (Dict, bool):
        if visited is None:
            visited = {}
        if self.is_offset(x, y):
            return visited, False
        if not self.is_land(x, y):
            return visited, False
        if visited.get(f"{x},{y}", False):
            return visited, True
        if self.is_mapped(x, y):
            return visited, True

        visited[f"{x},{y}"] = True
        for xx, yy in iter(self.next_neightbour(x, y)):
            self.find_land(xx, yy, visited)
            if self.is_offset(xx, yy):
                self.perimeter += 1
                continue
            if not self.is_land(xx, yy):
                self.perimeter += 1
                continue

        return visited, True

    def travel_map(self):
        for x, row in enumerate(self.grid):
            for y, col in enumerate(row):
                land, found = self.find_land(x, y)
                if found:
                    self.mapped_land.update(land)


    def calculate_perimeter(self) -> int:
        self.travel_map()
        return self.perimeter

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.grid = grid
        return self.calculate_perimeter()


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
    assert test_1() is True
