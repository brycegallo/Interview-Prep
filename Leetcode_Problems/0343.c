// LeetCode 0343 - Integer Break
// Medium - 1-D Dynamic Programming
// Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
// Return the maximum product you can get.

//  Dynamic Programming Solution
// Complexities:
// Time : O(n)
// Space: O(1)
int integerBreak(int n) {
    if (n <= 3) return n - 1;
    int result = 1;
    while (n > 4) { result *= 3, n -= 3; }
    return result * n;
}
