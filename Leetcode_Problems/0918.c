// LeetCode 0918 - Maximum Sum Circular Subarray
// Medium - Greedy
// Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
//
// A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
//
// A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
//
// Solution using Kadane's Algorithm
// Complexities:
// Time : O(n)
// Space: O(1)
int maxSubarraySumCircular(int* nums, int numsSize) {
    int global_max, global_min = global_max = nums[0];
    int current_max, current_min = current_max = 0;
    int total = 0;

    for (int i = 0; i < numsSize; i++) {
        current_max = nums[i] > (current_max + nums[i]) ? nums[i] : (current_max + nums[i]);
        current_min = nums[i] < (current_min + nums[i]) ? nums[i] : (current_min + nums[i]);
        total += nums[i];
        global_max = global_max > current_max ? global_max : current_max;
        global_min = global_min < current_min ? global_min : current_min;
    }

    return (global_max > 0 && total - global_min > global_max) ? (total - global_min) : global_max;
}
