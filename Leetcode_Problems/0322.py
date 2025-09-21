# LeetCode 0322 - Coin Change
# Medium - 1-D Dynamic Programming
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# 1-D Dynamic Programming Solution
# Complexities:
# Time : O(m * n) m = amount, n = coins
# Space: O(m)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in coins: return 1  # may not help that much
        cache = [amount + 1] * (amount + 1)  # amount + 1 acts as a max value
        cache[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                cache[a] = min(cache[a], 1 + cache[a - c]) if a - c >= 0 else cache[a]
        return cache[amount] if cache[amount] != amount + 1 else -1
