# LeetCode 0229 - Majority Element II
# Medium - Arrays & Hashing
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Hashing Solution
# Complexities:
# Time : O(n) - O(2n) - reduces to O(n)
# Space: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count, result = {}, []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key in count.keys():
            if count[key] > (len(nums) // 3):
                result.append(key)
        return result
