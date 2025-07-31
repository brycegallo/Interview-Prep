# LeetCode 0039 - Combination Sum
# Medium - Backtracking
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Recursive Depth-First Search Solution
# Complexities:
# Time : O(t / 2m) - where t = target and m is the minimum value in candidates
# Space: O(t / 2m) - same as Time
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, current, total):
            if total != target and not (index >= len(candidates) or total > target):
                current.append(candidates[index])
                dfs(index, current, total + candidates[index])  # run dfs() with current candidate
                current.pop()
                dfs(index + 1, current, total)  # run dfs() without current candidate
            elif total == target:
                result.append(current.copy())

        dfs(0, [], 0)
        return result

# (Optimized) Recursive Depth-First Search Solution with Sorting
# Complexities:
# Time : O(t / 2m) - where t = target and m is the minimum value in candidates
# Space: O(t / 2m) - same as Time
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(i, cur, total):
            if total != target:
                for j in range(i, len(candidates)):
                    if total + candidates[j] <= target:
                        cur.append(candidates[j])
                        dfs(j, cur, total + candidates[j])
                        cur.pop()
            else:
                result.append(cur.copy())

        dfs(0, [], 0)
        return result

