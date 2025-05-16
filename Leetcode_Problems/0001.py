# LeetCode 0001 - Two Sum
# Easy - Arrays & Hashing
# Given an array of integers num and an integer taraget, return the indices of the two numbers such that they add up to target
# You may assume that each input would have exactly one solution, and you may not use the same element twice
# You can return the answer in any order

# Hash Map Solution
# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap[difference] = index
        hashmap = {}

        for index, number in enumerate(nums):
            difference = target - number
            if difference in hashmap:
                return [hashmap[difference], index]
            hashmap[number] = index
