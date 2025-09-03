// LeetCode 0198 - House Robber
// Medium - 1D Dynamic Programming
// You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
// Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

// Iterative Dynamic Programming Solution
// Complexities:
// Time : O(n)
// Space: O(1)
int rob(int* nums, int numsSize) {
    int result_1, result_2 = result_1 = 0;
    for (int i = 0; i < numsSize; i++) {
        int temp = result_1 + nums[i] >= result_2 ? result_1 + nums[i] : result_2;
        result_1 = result_2, result_2 = temp;
    }
    return result_2;
}
