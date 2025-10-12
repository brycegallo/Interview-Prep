# LeetCode 0279 - Perfect Squares
# Medium - 1-D Dynamic Programming
# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# Bottom-Up One-Dimensional Dynamic Programming Solution
# Complexities:
# Time : O(n * sqrt(n))
# Space: O(n)
class Solution:
    def numSquares(self, n: int) -> int:
        cache = [n] * (n + 1)
        cache[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                cache[target] = min(cache[target], 1 + cache[target - square])
        return cache[n]
