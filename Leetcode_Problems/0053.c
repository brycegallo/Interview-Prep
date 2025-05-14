// LeetCode 0053 - Maximum Subarray
// Medium - Greedy
// Given an integer array nums, find the subarray with the largest sum, and return its sum

// Kadane's Algorithm (Tersest Syntax)
// Complexities:
// Time : O(n)
// Space: O(1)
int maxSubArray(int* nums, int numsSize) {
    int max_sum, current_sum = max_sum = nums[0];

    for (int i = 1; i < numsSize; i++) {
        current_sum = (current_sum < 0 ? 0 : current_sum) + nums[i];
        max_sum = max_sum < current_sum ? current_sum : max_sum;
    }
    return max_sum;
}

// Kadane's Algorithm (Verbose Syntax)
// same as above but more readable
int verboseMaxSubArray(int* nums, int numsSize) {
    int max_sum = nums[0];
    int current_sum = nums[0];

    for (int i = 1; i < numsSize; i++) {
        if (current_sum < 0) {
            current_sum = 0;
        }
        current_sum = current_sum + nums[i];
        if (max_sum < current_sum) {
            max_sum = current_sum;
        }
    }
    return max_sum;
}
