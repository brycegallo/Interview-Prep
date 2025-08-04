# LeetCode 0046 - Permutations
# Medium - Backtracking
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Recursive Solution
# Complexities:
# Time : O(n!) - reduced from O(n! * n^2)
# Space: O(n!) - reduced from O(n! * n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) != 0:
            result = []
            perms = self.permute(nums[1:])

            for perm in perms:
                for i in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, nums[0])
                    result.append(perm_copy)
            return result
        return [[]]

# Iterative Solution
# Complexities:
# Time : O(n!) - reduced from O(n! * n^2)
# Space: O(n!) - reduced from O(n! * n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, n)
                    new_perms.append(perm_copy)
            perms = new_perms
        return perms
