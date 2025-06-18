// LeetCode 0070 - Climbing Stairs
// Easy - 1-D Dynamic Programming
// You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

// Dynamic Programming Solution
// Complexities:
// Time : O(n)
// Space: O(1)
int climbStairs(int n) {
    int int_one, int_two = int_one = 1;

    for (int i = 1; i < n; i++) {
        int temp = int_one;
        int_one += int_two;
        int_two = temp;
    }
    return int_one;
}
