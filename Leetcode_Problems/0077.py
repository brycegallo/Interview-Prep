# LeetCode 0077 - Combinations
# Medium - Backtracking
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

# Recursive Backtracking Solution
# Complexities:
# Time : O(k * n!/((n-k)! * k!)) - where n is the number of elements and k is the number of elements to pick
# Space: O(k * n!/((n-k)! * k!)) - same as time

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            if len(current) != k:
                for i in range(start, n + 1):
                    backtrack(i + 1, current + [i])  # may be less efficient than appending/popping
            else:
                result.append(current.copy())
        backtrack(1, [])

        return result
