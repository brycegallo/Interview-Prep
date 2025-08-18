# LeetCode 2185 - Counting Words with a Given prefix
# Easy - Tries
# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.

# Brute Force Solution
# Complexities:
# Time : O(m * n) - m = length of words, n = length of pref
# Space: O(n) - because word[:len(pref)] creates a new string
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        result = 0

        for word in words:
            result = result + 1 if word[:len(pref)] == pref else result
        return result

