# LeetCode 0997 - Squares of a Sorted Array
# Easy - Two Pointers
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Two-Pointer Solution
# Complexities
# Time : O(n)
# Space: O(n) - for the output array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1
        return result[::-1]
