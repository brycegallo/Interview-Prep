# LeetCode 0217 - Contains Duplicate
# Easy - Arrays & Hashing
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Hash Set Solution
# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for number in nums:
            if number in seen:
                return True
            seen.add(number)
        return False
