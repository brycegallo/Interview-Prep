# LeetCode 0073 - Set Matrix Zeroes
# Medium - Math & Geometry
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Solution
# Complexities:
# Time : O(m * n)
# Space: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        row_zero = False

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        row_zero = True
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        if matrix[0][0] == 0:
            for row in range(rows):
                matrix[row][0] = 0
        if row_zero:
            for col in range(cols):
                matrix[0][col] = 0
