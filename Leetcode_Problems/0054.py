# LeetCode 0054 - Spiral Matrix
# Medium - Math & Geometry
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Solution
# Complexities:
# Time : O(m * n)
# Space: O(1) - not counting output array, otherwise O(m*n)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right, output = 0, len(matrix), 0, len(matrix[0]), []

        while left < right and top < bottom:
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                output.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            for i in range(right - 1, left - 1, -1):
                output.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                output.append(matrix[i][left])
            left += 1
        return output
