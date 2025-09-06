# LeetCode 2706 - Buy Two Chocolates
# Easy - Greedy
# You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.
# You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.
# Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.

# Iterative Greedy Solution
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_1 = min_2 = float("inf")

        for price in prices:
            if price < min_1:
                min_1, min_2 = price, min_1
            elif price < min_2:
                min_2 = price
        leftover = money - (min_1 + min_2)

        return leftover if leftover >= 0 else money

