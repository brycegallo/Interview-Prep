// LeetCode 0121 - Best Time to Buy and Sell Stock
// Easy - Sliding Window
// You are given an array prices where prices[i] is the price of a given stock on the ith day.
// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

// Solution
// Complexities:
// Time : O(n)
// Space: O(1)
func maxProfit(prices []int) int {
    left, right, max_profit := 0, 1, 0

    for right < len(prices) {
        if prices[left] < prices[right] {
            profit := prices[right] - prices[left]
            if profit > max_profit {
                max_profit = profit
            }
        } else {
            left = right
        }
        right++
    }
    return max_profit
}
