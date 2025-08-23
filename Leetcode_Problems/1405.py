# LeetCode 1405 - Longest Happy String
# Medium - Heap / Priority Queue
# A string s is called happy if it satisfies the following conditions:
#    s only contains the letters 'a', 'b', and 'c'.
#    s does not contain any of "aaa", "bbb", or "ccc" as a substring.
#    s contains at most a occurrences of the letter 'a'.
#    s contains at most b occurrences of the letter 'b'.
#    s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
# A substring is a contiguous sequence of characters within a string.

# Greedy Min-Heap Solution
# Complexities:
# Time : O(n)
# Space: O(1) - O(n) for the output string
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result, max_heap = "", []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(max_heap, (count, char))

        while max_heap:
            count, char = heapq.heappop(max_heap)
            if len(result) > 1 and result[-1] == result[-2] == char:
                if not max_heap:
                    break
                count2, char2 = heapq.heappop(max_heap)
                result += char2
                count2 += 1
                if count2:
                    heapq.heappush(max_heap, (count2, char2))
            else:
                result += char
                count += 1
            if count:
                heapq.heappush(max_heap, (count, char))

        return result

