# LeetCode 0139 - Word Break
# Medium - 1-D Dynamic Programming
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Bottom-Up One-Dimensional Dynamic Programming Solution
# Complexities:
# Time : O(m * n * t) m = number of words in wordDict, n = length of s, t = length of longest word
# Space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [False] * (len(s) + 1)
        cache[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    cache[i] = cache[i + len(word)]
                    if cache[i]:
                        break
        return cache[0]
