# LeetCode 0033 - Search in Rotated Sorted Array
# Medium - Binary Search
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.

# Single Pass Binary Search Solution
# Complexities:
# Time : O(log n)
# Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                return middle

            if (nums[middle] >= nums[left] and (target > nums[middle] or target < nums[left])) or not (target < nums[middle] or target > nums[right]):
                left = middle + 1
            else:
                right = middle - 1

        return -1
