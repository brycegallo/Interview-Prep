# LeetCode 0256 - Paint House
# Medium - 1-D Dynamic Programming
# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
#     For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
# Return the minimum cost to paint all houses.

# Dynamic Programming Solution
# Complexities:
# Time : O(n) - O(n * 3) reducing to O(n)
# Space: O(n)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # costs[i][j], i = house, j = color
        cache = [0, 0, 0]
        for i in range(len(costs)):
            cache_0 = costs[i][0] + min(cache[1], cache[2])
            cache_1 = costs[i][1] + min(cache[0], cache[2])
            cache_2 = costs[i][2] + min(cache[0], cache[1])
            cache = [cache_0, cache_1, cache_2]
        return min(cache)
