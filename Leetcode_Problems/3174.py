# LeetCode 3174 - Clear Digits
# Easy - Stack
# You are given a string s.
# Your task is to remove all digits by doing this operation repeatedly:
#    Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.
# Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.

class Solution:
    def clearDigits(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            if s[i].isalpha():
                result.append(s[i])
            if s[i].isdigit() and result:
                result.pop()
        return "".join(result)
