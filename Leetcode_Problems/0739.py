# LeetCode 0739 - Daily Temperatures
# Medium - Stack
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Stack Solution
# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, stackIndex = stack.pop()
                answer[stackIndex] = (index - stackIndex)
            stack.append([temp, index])
        return answer

