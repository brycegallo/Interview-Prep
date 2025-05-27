# LeetCode 0560 - Subarray Sum Equals K
# Medium - Arrays & Hashing
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

# Single-Pass Greedy Hashing Solution
# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result, current_sum = 0, 0
        prefix_sums = { 0 : 1}

        for number in nums:
            current_sum += number
            difference = current_sum - k
            result += prefix_sums.get(difference, 0)
            prefix_sums[current_sum] = 1 + prefix_sums.get(current_sum, 0)

        return result
