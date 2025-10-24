# LeetCode 0059 - Spiral Matrix II
# Medium - Math & Geometry
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

# Solution
# Complexities:
# Time : O(n^2)
# Space: O(1) - not counting output array, otherwise O(n^2)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        value, top, left, bottom, right = 1, 0, 0, n - 1, n - 1

        while left <= right:
            for column in range(left, right + 1):
                matrix[top][column], value = value, value + 1
            top += 1

            for row in range(top, bottom + 1):
                matrix[row][right], value = value, value + 1
            right -= 1

            for column in range(right, left - 1, -1):
                matrix[bottom][column], value = value, value + 1
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                matrix[row][left], value = value, value + 1
            left += 1
        return matrix
