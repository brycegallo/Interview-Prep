# LeetCode 0189 - Rotate Array
# Medium - Two Pointers
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Four Pointer Solution using reverse() builtin
# Complexities:
# Time : O(n) - O(2n) really, O(n) to reverse and O(n) to reverse two subarrays, reducing to O(n)
# Space: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        left_left, left_right = 0, k - 1
        right_left, right_right = k, len(nums) - 1

        while left_left < left_right:
            nums[left_left], nums[left_right] = nums[left_right], nums[left_left]
            left_left += 1
            left_right -= 1

        while right_left < right_right:
            nums[right_left], nums[right_right] = nums[right_right], nums[right_left]
            right_left += 1
            right_right -= 1
