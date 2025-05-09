# Leetcode 1929 - Concatenation of Array
# Easy - Arrays and Hashing
# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.


# Single-Pass Solution
# Complexities: 
# Time : O(n)
# Memory: O(n)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        result = [0] * nums_len * 2

        for i in range(nums_len):
            result[i] = result[i+nums_len] = nums[i]
        return result

# Alternative solution, same as above but in one line
class AltSolution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
