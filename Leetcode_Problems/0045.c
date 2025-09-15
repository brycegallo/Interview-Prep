// LeetCode 0045 - Jump Game II
// Medium - Greedy
// You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
// Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:
//    0 <= j <= nums[i] and
//    i + j < n
// Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

// Greedy Iterative Solution
// Complexities:
// Time : O(n)
// Space: O(1) 
int jump(int* nums, int numsSize) {
    int result = 0, left = 0, right = 0;
    
    while (right < numsSize - 1) {
        int furthest = 0;
        for (int i = left; i < right + 1; i++) {
            furthest = i + nums[i] > furthest ? i + nums[i] : furthest;
        }
        left = ++right, right = furthest, result++;
    }
    return result;
}
