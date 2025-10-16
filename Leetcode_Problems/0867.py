# LeetCode 0867 - Transpose Matrix
# Easy - Math & Geometry
# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

# Solution
# Complexities:
# Time : O(m * n)
# Space: O(m * n)
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        result = [[0] * rows for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                result[col][row] = matrix[row][col]
        return result
