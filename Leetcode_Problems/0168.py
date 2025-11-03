# LeetCode 0168 - Excel Sheet Column Title
# Easy - Math & Geometry
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# Solution
# Complexities:
# Time : O(log26 n)
# Space: O(1)
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            result += chr(ord('A') + offset)
            columnNumber = (columnNumber - 1) // 26
        return result[::-1]
