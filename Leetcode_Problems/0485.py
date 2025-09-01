# LeetCode 0485 - Max Consecutive Ones
# Easy - Arrays & Hashing
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Iterative Solution
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = current = 0

        for i in range(len(nums)):
            current = current + 1 if nums[i] == 1 else 0
            result = max(result, current)
        return result
