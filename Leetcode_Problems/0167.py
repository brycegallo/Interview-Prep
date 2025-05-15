# LeetCode 0167 - Two Sum II - Input Array is Sorted
# Medium - Two Pointers
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
#
# Your solution must use only constant extra space.

# Two-Pointer Solution
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            if target < numbers[left] + numbers[right]:
                right -= 1
            elif target > numbers[left] + numbers[right]:
                left += 1
            else:
                return [left + 1, right + 1]
