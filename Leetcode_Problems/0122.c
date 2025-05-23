// LeetCode 0122 - Best Time to Buy and Sell Stock II
// Medium - Arrays & Hashing (actually easy)
// You are given an array prices where prices[i] is the price of a given stock on the ith day.
//
// On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
//
// Return the maximum profit you can achieve.

// Single-Pass Iterative Solution
// Complexities:
// Time : O(n)
// Space: O(1)
// Terse
int maxProfit(int* prices, int pricesSize) {
    int total_profit = 0;

    for (int i = 0; i < pricesSize - 1; i++) {
        total_profit += prices[i] < prices[i + 1] ? (prices[i + 1] - prices[i]) : 0;
    }
    return total_profit;
}
// Verbose (Slightly)
int maxProfit(int* prices, int pricesSize) {
    int total_profit = 0;

    for (int i = 0; i < pricesSize - 1; i++) {
        if (prices[i] < prices[i + 1]) {
            total_profit += (prices[i + 1] - prices[i]);
        }
    }
    return total_profit;
}
