# LeetCode 0152 - Maximum Product Subarray
# Medium - 1-D Dynamic Programming
# Given an integer array nums, find a subarray that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.

# One-Dimensional Dynamic Programming Solution
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result, cur_min, cur_max = max(nums), 1, 1

        for num in nums:
            cur_max, cur_min = max(num * cur_max, num * cur_min, num), min(num * cur_max, num * cur_min, num)
            result = max(result, cur_max)
        return result
