# LeetCode 0045 - Jump Game II
# Medium - Greedy
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:
#    0 <= j <= nums[i] and
#    i + j < n
# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

# Greedy Iterative Solution
# Complexities:
# Time : O(n)
# Space: O(1) 
class Solution:
    def jump(self, nums: List[int]) -> int:
        result = left = right = 0

        while right < len(nums) - 1:
            furthest = 0
            for i in range(left, right + 1):
                furthest = max(furthest, i + nums[i])
            left, right, result = right + 1, furthest, result + 1
        return result

