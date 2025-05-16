# LeetCode 0128 - Longest Consecutive Sequence
# Medium - Arrays & Hashing
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.

# Hash Set Solution
# Complexities:
# Time : O(n) - worst case scenario O(2n) reducing to O(n)
# Space: O(n) - set could potentially be as large as array
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0

        for number in num_set:
            if number - 1 not in num_set:
                count = 0
                while number in num_set:
                    count += 1
                    max_count = max(max_count, count)
                    number += 1
        return max_count
