# LeetCode 0040 - Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.

# Recursive Backtracking Solution
# Complexities:
# Time : O(n * 2^n)
# Space: O(n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(i, current, total):
            if total != target and not (total > target or i >= len(candidates)):
                current.append(candidates[i])
                dfs(i + 1, current, total + candidates[i])
                current.pop()
                while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
                dfs(i + 1, current, total)
            if total == target:
                result.append(current.copy())
        dfs(0, [], 0)
        return result
