# LeetCode 0048 - Rotate Image
# Medium - Math & Geometry
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Solution
# Complexities:
# Time : O(n^2)
# Space: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                top_left = matrix[top][left + i]  # save the top left value to allow in-place modification
                matrix[top][left + i] = matrix[bottom - i][left]  # move bottom left into top left
                matrix[bottom - i][left] = matrix[bottom][right - i]  # move bottom right into bottom left
                matrix[bottom][right - i] = matrix[top + i][right]  # move top right into bottom right
                matrix[top + i][right] = top_left  # move top left into top right
            left, right = left + 1, right - 1
