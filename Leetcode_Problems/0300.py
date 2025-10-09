# LeetCode 0300 - Longest Increasing Subsequence
# Medium - 1-D Dynamic Programming
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Bottom-Up One-Dimensional Dynamic Programming Solution
# Complexities:
# Time : O(n^2)
# Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        result = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    result[i] = max(result[i], 1 + result[j])
        return max(result)
