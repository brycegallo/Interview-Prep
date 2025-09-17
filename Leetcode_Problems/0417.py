# LeetCode 0417 - Pacific Atlantic Water Flow
# Medium - Graphs
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Depth-First Search Solution
# Complexities:
# Time : O(m * n) - m = rows, n = columns
# Space: O(m * n)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        result = []

        def dfs(row, col, visit_set, prev_height):
            if ((row, col) in visit_set or row < 0 or col < 0 or row == ROWS or col == COLS or heights[row][col] < prev_height):
                return
            visit_set.add((row, col))
            dfs(row + 1, col, visit_set, heights[row][col])
            dfs(row - 1, col, visit_set, heights[row][col])
            dfs(row, col + 1, visit_set, heights[row][col])
            dfs(row, col - 1, visit_set, heights[row][col])

        for col in range(COLS):
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])

        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLS - 1, atl, heights[row][COLS - 1])

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pac and (row, col) in atl:
                    result.append((row, col))

        return result
