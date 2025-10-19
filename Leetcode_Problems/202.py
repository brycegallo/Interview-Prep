# LeetCode 0202 - Insert Greatest Common Divisors in Linked List
# Easy - Math & Geometry
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Solution
# Complexities:
# Time : O(log n)
# Space: O(log n)
class Solution:
    def sumOfSquares(self, n:int) -> int:
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output
    
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
        return True if n == 1 else False
