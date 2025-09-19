# LeetCode 0647 - Palindromic Substrings
# Medium - Two Pointers
# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Two-Pointer Solution
# Complexities:
# Time: O(n^2)
# Space: O(1)
class Solution:
    def find_palindromes(self, s, left, right):
            result = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result, left, right = result + 1, left - 1, right + 1
            return result

    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.find_palindromes(s, i, i)  # find even-length palindromes
            result += self.find_palindromes(s, i, i + 1)  # find odd-length palindromes
        return result
