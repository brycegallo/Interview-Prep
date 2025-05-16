# LeetCode 0242: Valid Anagram
# Easy - Arrays & Hashing
# Given two strings s and t, return true if t is an anagram of s, and false otherwise
# s is guaranteed to be at least 1 character, t is not

# Hash Map Solution
# Complexities:
# Time : O(m + n)
# Space: O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if strings are not the same length, they can't be anagrams
        if len(s) != len(t):
            return False
        
        # create empty hash maps ("dictionaries" in python)
        s_map, t_map = {}, {}

        for i in range(len(s)):
            # set key and value = 1 + current value (will be 0 if not present)
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        return s_map == t_map
