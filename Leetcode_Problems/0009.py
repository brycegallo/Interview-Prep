# LeetCode 0009 - Palindrome Number
# Easy - Math & Geometry
# Given an integer x, return true if x is a palindrome, and false otherwise.

# Solution
# Complexities:
# Time : O(1)
# Space: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            dividor = 1
            while x >= 10 * dividor:
                dividor *= 10
            while x:
                if x // dividor != x % 10: return False
                x = (x % dividor) // 10
                dividor = dividor / 100
        return False if x < 0 else True
