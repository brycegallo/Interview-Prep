# LeetCode 1481 - Least Number of Unique Integers after K Removals
# Medium - Heap / Priority Queue
# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

# Min-Heap Solution
# Complexities
# Time : O(n * log n)
# Space: O(n)
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        heap = list(freq.values())
        heapq.heapify(heap)

        result = len(heap)
        while k > 0 and heap:
            f = heapq.heappop(heap)
            if k >= f:
                k -= f
                result -= 1
        return result

# Bucket Sort Solution without Min-Heap
# Complexities
# Time : O(n)
# Space: O(n)
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        freq_list = [0] * (len(arr) + 1)  # freq -> # of elements with that freq

        for _, f in freq.items():
            freq_list[f] += 1

        result = len(freq)
        for f in range(1, len(freq_list)):
            remove = freq_list[f]
            if k >= f * remove:
                k, result = k - f * remove, result - remove
            else:
                return result - k // f
        return result
