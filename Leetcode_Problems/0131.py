# LeetCode 0131 - Palindrome Partitioning
# Medium - Backtracking
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# Backtracking Solution
# Complexities:
# Time : O(n * 2^n)
# Space: O(n) - O(n * 2^n) for the output list
class Solution:
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        result, partition = [], []

        def dfs(i):
            if i >= len(s):
                result.append(partition.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    partition.append(s[i:j + 1])
                    dfs(j + 1)
                    partition.pop()

        dfs(0)
        return result
