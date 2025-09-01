# LeetCode 0205 - Isomorphic Strings
# Easy - Arrays & Hashing
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Iterative Solution with HashMaps
# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st, map_ts = {}, {}

        for i in range(len(s)):
            if s[i] in map_st and map_st[s[i]] != t[i] or t[i] in map_ts and map_ts[t[i]] != s[i]:
                return False
            map_st[s[i]], map_ts[t[i]] = t[i], s[i]
        return True
