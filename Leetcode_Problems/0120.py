# LeetCode 0120 - Triangle
# Medium - 1-D Dynamic Programming
# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

# Dynamic Programming Solution
# Complexities:
# Time : O(n^2)
# Space: O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        cache = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                cache[i] = n + min(cache[i], cache[i + 1])
        return cache[0]
