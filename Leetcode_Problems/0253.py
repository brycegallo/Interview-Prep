# LeetCode 0253 - Meeting Rooms
# Medium - Intervals
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Solution
# Complexities:
# Time : O(n logn)
# Space: O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        result = count = start = end = 0
        while start < len(intervals):
            if start_times[start] < end_times[end]:
                start, count = start + 1, count + 1
            else:
                end, count = end + 1, count - 1
            result = max(result, count)
        return result
