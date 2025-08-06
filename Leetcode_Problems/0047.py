# LeetCode 0047 - Permutations II
# Medium - Backtracking
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Recursive Depth-First Search Solution
# Complexities:
# Time : O(n! * n)
# Space: O(n! * n) - for the output list
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result, perm = [], []
        count = {n: 0 for n in nums}
        for n in nums:
            count[n] += 1

        def dfs():
            if len(perm) != len(nums):
                for n in count:
                    if count[n] > 0:
                        perm.append(n)
                        count[n] -= 1
                        dfs()
                        count[n] += 1
                        perm.pop()
            else:
                result.append(perm.copy())
        dfs()
        return result
