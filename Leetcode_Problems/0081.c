// LeetCode 0081 - Search in Rotated Sorted Array II
// Medium - Binary Search
// There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
//
// Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
//
// Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
//
// You must decrease the overall operation steps as much as possible.

// Binary Search Solution Augmented with Linear Scanning
// Complexities:
// Time : O(n) - worst case, normally O(log n)
// Space: O(1)
bool search(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize - 1;

    while (left <= right) {
        int middle = left + (right - left) / 2;
        if (nums[middle] == target) {
            return true;
        }

        if (nums[left] < nums[middle]) {
            if (nums[left] <= target && target < nums[middle]) {
                right = --middle;
            }
            else {
                left = ++middle;
            }
        } else if (nums[left] > nums[middle]) {
            if (nums[middle] < target && target <= nums[right]) {
                left = ++middle;
            } else {
                right = --middle;
            }
        } else {
            left++;
        }
    }
    return false;
}
