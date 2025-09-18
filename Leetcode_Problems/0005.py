# LeetCode 0005 - Longest Palindromic Substring
# Medium - Two Pointers
# Given a string s, return the longest palindromic in s.

# Two-Pointer Solution
# Complexities:
# Time : O(n^2)
# Space: O(1) - O(n) for the output string
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result_index, result_length = 0, 0

        def find_palindromes(left, right):
            nonlocal result_length, result_index
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > result_length:
                    result_index, result_length = left, right - left + 1
                left, right = left - 1, right + 1

        for i in range(len(s)):
            find_palindromes(i, i)
            find_palindromes(i, i + 1)

        return s[result_index:result_index + result_length]
