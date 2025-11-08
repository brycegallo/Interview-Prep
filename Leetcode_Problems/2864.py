# LeetCode 2864 - Maximum Odd Binary Number
# Easy - Greedy
# You are given a binary string s that contains at least one '1'.
# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.
# Return a string representing the maximum odd binary number that can be created from the given combination.
# Note that the resulting string can have leading zeros.

# Greedy Solution
# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        for char in s:
            count = count + 1 if char == "1" else count
        return (count - 1) * "1" + (len(s) - count) * "0" + "1"
