# LeetCode 0050 - Pow(x,n)
# Medium - Math & Geometry
# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Solution
# Complexities:
# Time : O(log n)
# Space: O(log n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            result = 1 if n == 0 else helper(x * x, n // 2)
            return x * result if n % 2 or x == 0 else result
        return helper(x, abs(n)) if n >= 0 else 1 / helper(x, abs(n))
