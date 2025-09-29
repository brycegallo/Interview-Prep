# LeetCode 0252 - Meeting Rooms
# Easy - Intervals
# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

# Solution
# Complexities:
# Time : O(n logn) - due to sorting algorithm
# Space: O(n) or O(1) - depending on sorting algorithm
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i : i[0])
        for i in range(1, len(intervals)):
            if (intervals[i - 1][1] > intervals[i][0]):
                return False
        return True
