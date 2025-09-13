# LeetCode 1762 - Buildings With an Ocean View
# Medium - Greedy
# There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
# The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.
# Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

# Greedy Iterative Solution
# Complexities:
# Time : O(n)
# Space: O(n) - O(1) but O(n) for the output list
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = [len(heights) - 1]

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > heights[result[-1]]:
                result.append(i)
        return result[::-1]
