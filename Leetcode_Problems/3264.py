# LeetCode 3264 - Final Array State after K Multiplication Operations I
# Easy - Heap / Priority Queue
# You are given an integer array nums, an integer k, and an integer multiplier.
# You need to perform k operations on nums. In each operation:
#    Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
#    Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.

# Min-Heap Solution
# Complexities:
# Time : O(k * log n)
# Space: O(n)
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        result = nums[::]

        min_heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(min_heap)

        for _ in range(k):
            n, i = heapq.heappop(min_heap)
            result[i] *= multiplier
            heapq.heappush(min_heap, (result[i], i))
        return result

