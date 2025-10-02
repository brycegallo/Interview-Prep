# LeetCode 0056 - Merge Intervals
# Medium - Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Solution
# Complexities:
# Time : O(n logn)
# Space: O(n) - could be O(1) or O(n) depending on sorting algorithm, O(n) for output list
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = output[-1][1]
            if start <= last_end:
                output[-1][1] = max(last_end, end)
            else:
                output.append([start, end])
        return output
