# LeetCode 1267 - Count Servers that Communicate
# Medium - Graphs
# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.

# Iterative Solution
# Complexities:
# Time : O(m*n) - m, n = number of rows, columns in grid
# Space: O(m+n)
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        row_count = [0] * ROWS  # index = row -> value = count
        col_count = [0] * COLS  # index = col -> value = count

        # Pre-Processing: setting up row and col count arrays for quick checking
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    row_count[row] += 1
                    col_count[col] += 1

        result = 0
        for row in range(ROWS):
            for col in range(COLS):
                # if grid[row][col] and row_count[row] > 1 or col_count[col] > 1:
                if grid[row][col] and max(row_count[row], col_count[col]) > 1:
                    result += 1
        return result
