# LeetCode 0435 - Non-Overlapping Intervals
# Medium - Intervals
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

# Greedy Solution
# Complexities:
# Time : O(n logn)
# Space: O(n) - or O(1) depending on sorting algorithm
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        result, prev_end = 0, intervals[0][1]
        for start, end in intervals[1:]:
            result = result if start >= prev_end else result + 1
            prev_end = end if start >= prev_end else min(end, prev_end)
        return result
