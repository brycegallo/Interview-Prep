// LeetCode 0213 - House Robber II
// Medium - 1D Dynamic Programming
// You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
// Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

// Iterative Dynamic Programming Solution
// Complexities:
// Time : O(n)
// Space: O(1)
int rob_old(int* nums, int index, int numsSize) {
    int result_1, result_2 = result_1 = 0;

    for (int i = index; i < numsSize; i++) {
        int temp = result_1 + nums[i] > result_2 ? result_1 + nums[i] : result_2;
        result_1 = result_2, result_2 = temp;
    }
    return result_2;
}

int rob(int* nums, int numsSize) {
    int result_1 = rob_old(nums, 0, numsSize - 1), result_2 = rob_old(nums, 1, numsSize);
    result_1 = nums[0] > result_1 ? nums[0] : result_1;
    return result_1 > result_2 ? result_1 : result_2;
}
