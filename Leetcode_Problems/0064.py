# LeetCode 0064 - Minimum Path Sum
# Medium - 2-D Dynamic Programming
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.

# 2-D Dynamic Programming Solution (Caching)
# Complexities:
# Time : O(m * n) - m = rows, n = columns
# Space: O(m * n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        result = [[float("inf")] * (COLS + 1) for row in range(ROWS + 1)]
        result[ROWS - 1][COLS] = 0

        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                result[row][col] = grid[row][col] + min(result[row + 1][col], result[row][col + 1])
        return result[0][0]
