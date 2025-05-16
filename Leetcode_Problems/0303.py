# LeetCode 0303 - Range Sum Query - Immutable
# Easy - Arrays & Hashing
# Given an integer array nums, handle multiple queries of the following type:
# 1. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
#   NumArray(int[] nums) Initializes the object with the integer array nums.
#   int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
#
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Iterative Solution using Prefix Array
# Complexities:
# Time : O(n)
# Space: O(n)
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_array = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.prefix_array.append(total)
        
        
    def sumRange(self, left: int, right: int) -> int:
        prefix_right = self.prefix_array[right]
        prefix_left = self.prefix_array[left - 1] if left > 0 else 0
        return prefix_right - prefix_left
