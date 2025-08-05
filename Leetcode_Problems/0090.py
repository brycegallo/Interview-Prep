# LeetCode 0090 - Subsets II
# Medium - Backtracking
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Recursive Solution
# Complexities:
# Time : O(n * 2^n)
# Space: O(2^n) - for the output, O(n) extra space
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i, subset):
            if i != len(nums):
                subset.append(nums[i])
                backtrack(i + 1, subset)  # All subsets including i
                subset.pop()
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    i += 1
                backtrack(i + 1, subset)  # All subsets excluding i
            else:
                result.append(subset.copy())

        backtrack(0, [])
        return result

# Iterative Solution
# Complexities:
# Time : O(n * 2^n)
# Space: O(2^n) - for the output, O(1) extra space
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()
        prev_idx = idx = 0

        for i in range(len(nums)):
            idx = prev_idx if i >= 1 and nums[i] == nums[i - 1] else 0
            prev_idx = len(result)
            for j in range(idx, prev_idx):
                temp = result[j].copy()
                temp.append(nums[i])
                result.append(temp)
        return result
