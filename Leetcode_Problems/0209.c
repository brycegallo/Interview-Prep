// LeetCode 0209 - Minimum Size Subarray Sum
// Medium - Sliding Window
// Given an array of positive integers nums and a positive integer target, return the minimal length of a whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

// Sliding Window Solution
// Complexities:
// Time : O(n)
// Space: O(1)
int minSubArrayLen(int target, int* nums, int numsSize) {
    int left, sum = left = 0;
    int min_len = numsSize + 1;

    for (int right = 0; right < numsSize; right++) {
        sum += nums[right];
        while(sum >= target) {
            min_len = (min_len < right - left + 1) ? min_len : (right - left + 1);
            sum -= nums[left++];
        }
    }
    return min_len > numsSize ? 0 : min_len;
}
