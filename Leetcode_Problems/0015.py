# LeetCode 0015 - 3Sum
# Medium - Two Pointers
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Two Pointer - Nested Loop, Sorting Solution
# Complexities:
# Time : O(n^2) - O(n logn) for sorting and O(n^2) for iterating over the list n * n times
# Space: O(n) - worst case scenario, depending on the sorting algorithm used, could be O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, number in enumerate(nums):
            if not (i > 0 and number == nums[i - 1]):
                left, right = i + 1, len(nums) - 1
                while left < right:
                    three_sum = number + nums[left] + nums[right]
                    if three_sum > 0:
                        right -= 1
                    elif three_sum < 0:
                        left += 1
                    else:
                        result.append([number, nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1

        return result
