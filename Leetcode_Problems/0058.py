# LeetCode 0058 - Length of Last Word
# Easy - Arrays & Hashing
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Iterative Solution
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            length, i = length + 1, i - 1
        return length
