# LeetCode 0767 - Reorganize String
# Medium - Heap / Priority Queue
# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.

# Min-Heap Solution
# Complexities:
# Time : O(n * log n)
# Space: O(1) - O(n) for the output string
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [[-count, char] for char, count in count.items()]
        heapq.heapify(max_heap)

        previous = None
        result = ""
        while max_heap or previous:
            if not max_heap:
                return ""
            count, char = heapq.heappop(max_heap)
            result += char
            count += 1

            if previous:
                heapq.heappush(max_heap, previous)
                previous = None

            previous = [count, char] if count != 0 else previous

        return result

