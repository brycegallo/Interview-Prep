# LeetCode 2326 - Spiral Matrix IV
# Medium - Math & Geometry
# You are given two integers m and n, which represent the dimensions of a matrix.
# You are also given the head of a linked list of integers.
# Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
# Return the generated matrix.
# You are also given the head of a linked list of integers.
# Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
# Return the generated matrix.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution
# Complexities:
# Time : O(m * n)
# Space: O(1) - not counting output array, otherwise O(m*n)
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        top, left, right, bottom = 0, 0, n, m
        grid = [[-1] * n for _ in range(m)]

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, col, direction = 0, 0, 0
        while head:
            d_row, d_col = directions[direction]
            while (head and left <= col < right and top <= row < bottom and grid[row][col] == -1):
                grid[row][col], head = head.val, head.next
                row, col = row + d_row, col + d_col
            row, col = row - d_row, col - d_col
            direction = (direction + 1) % 4
            d_row, d_col = directions[direction]
            row, col = row + d_row, col + d_col
        return grid
