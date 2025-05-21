# LeetCode 0118 - Pascal's Triangle
# Easy - Uncategorized
# Given an integer numRows, return the first numRows of Pascal's triangle.
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
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            temp_result = [0] + copy.deepcopy(result[i - 1]) + [0]
            current_row = []
            for i in range(0, len(temp_result) - 1):
                current_row.append(temp_result[i] + temp_result[i+1])
            result.append(current_row)
        return result
