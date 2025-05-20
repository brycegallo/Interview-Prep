# Leetcode 0347 - Top K Frequent Elements
# Medium - Arrays & Hashing
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Bucket Sort Solution with Hashmap
# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for number in nums:
            count[number] = 1 + count.get(number, 0)
        for number, num_count in count.items():
            frequency[num_count].append(number)

        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for number in frequency[i]:
                result.append(number)
                if len(result) == k:
                    return result
