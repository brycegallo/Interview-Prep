# LeetCode 0215 - Kth Largest Element in Array
# Medium - Heap / Priority Queue
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

# Iterative Solution with Min Heap
# Complexities:
# Time: O(n * log k)
# Space: O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)
