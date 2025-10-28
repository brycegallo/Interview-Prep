# LeetCode 0342 - Power of Four
# Easy - Math & Geometry
# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4^x.

# Solution
# Complexities:
# Time : O(1) - depending on implementation of log() function
# Space: O(1)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n , 4) % 1 == 0
