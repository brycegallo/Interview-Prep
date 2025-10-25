# LeetCode 0885 - Spiral Matrix III
# Medium - Math & Geometry
# You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.
# You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.
# Return an array of coordinates representing the positions of the grid in the order you visited them.

# Solution
# Complexities:
# Time : O(m*n) - m = rows, n = cols
# Space: O(1) - not counting output array, otherwise O(m*n)
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # row, column delta pairs
        result, row, col = [], rStart, cStart
        steps, i = 1, 0

        while len(result) < rows * cols:
            for _ in range(2):
                delta_row, delta_col = directions[i]
                for _ in range(steps):
                    if (0 <= row < rows and 0 <= col < cols):
                        result.append([row, col])
                    row, col = row + delta_row, col + delta_col
                i = (i + 1) % 4
            steps += 1
        return result
