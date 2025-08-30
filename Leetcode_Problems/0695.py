# LeetCode 0695 - Max Area of Island
# Medium - Graphs
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

# Depth-First Search Solution with Hash Set
# Complexities:
# Time : O(m * n) - m is the number of rows, n is the number of columns
# Space: O(m * n)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if (row < 0 or row == ROWS or col < 0 or col == COLS or grid[row][col] == 0 or (row, col) in visited):
                return 0
            visited.add((row, col))
            return (1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))

        result = 0
        for row in range(ROWS):
            for col in range(COLS):
                result = max(result, dfs(row, col))

        return result
