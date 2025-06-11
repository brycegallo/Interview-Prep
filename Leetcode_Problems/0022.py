# LeetCode 0022 - Generate Parentheses
# Medium - Stack
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Recursive Solution Using a Stack
# Complexities:
# Time : O(4^n / sqrt(n))
# Space: O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                result.append("".join(stack))
                return
            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()

        backtrack(0, 0)
        return result
