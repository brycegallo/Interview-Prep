# LeetCode 0119 - Pascal's Triangle
# Easy - Uncategorized
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#     [1]
#    [1,1]
#   [1,2,1]
#  [1,3,3,1]
# [1,4,6,4,1]

# Iterative Solution
# Complexities:
# Time : O(k * n)
# Space: O(k * n)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]

        for i in range(rowIndex):
            next_row = [0] * (len(result) + 1)
            for j in range(len(result)):
                next_row[j] += result[j]
                next_row[j+1] += result[j]
            result = next_row
        return result
