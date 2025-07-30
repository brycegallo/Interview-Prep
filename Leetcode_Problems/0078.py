# LeetCode 0078 - Subsets
# Medium - Backtracking
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Recursive Depth-First Search Solutionn
# Complexities:
# Time : O(n * 2^n)
# Space: O(n) - O(2^n) for output list
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, subset = [], []

        def dfs(i):
            if i < len(nums):
                subset.append(nums[i])  # include nums[i] and run dfs()
                dfs(i + 1)
                subset.pop()  # don't include nums[i] and run dfs()
                dfs(i + 1)
            else:
                result.append(subset.copy())
        dfs(0)
        return result

# Iterative Solutionn
# Complexities:
# Time : O(n * 2^n)
# Space: O(n) - O(2^n) for output list
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            result += [subset + [num] for subset in result]

        return result
