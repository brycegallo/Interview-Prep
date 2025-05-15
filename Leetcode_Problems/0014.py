# LeetCode 0014 - Longest Common Prefix
# Easy - Arrays & Hashing
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Iterative Solution (without extra space by returning slice at tracked index)
# Complexities:
# Time : O(m * n)
# Space: O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return word[:i]
        return strs[0]
