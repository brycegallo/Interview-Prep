# LeetCode 0416 - Partition Equal Subset Sum
# Medium - 1-D Dynamic Programming
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# Bottom-Up One-Dimensional Dynamic Programming Solution
# Complexities:
# Time : O(n * target)
# Space: O(n * target)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        cache = set()
        cache.add(0)
        if target % 2 == 0:
            target = target // 2
            for i in range(len(nums) - 1, -1, -1):
                next_cache = set()
                for total in cache:
                    if (total + nums[i]) == target: return True  # optional optimization
                    next_cache.add(total)
                    next_cache.add(total + nums[i])
                cache = next_cache
        return True if target in cache else False
