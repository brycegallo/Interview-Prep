// LeetCode 0153 - Find Minimum in Rotated Sorted Array
// Medium - Binary Search
// Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
//    [4,5,6,7,0,1,2] if it was rotated 4 times.
//    [0,1,2,4,5,6,7] if it was rotated 7 times.
// Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
// Given the sorted rotated array nums of unique elements, return the minimum element of this array.
// You must write an algorithm that runs in O(log n) time.

// Binary Search Solution
// Complexities:
// Time : O(logn)
// Space: O(1)
int findMin(int* nums, int numsSize) {
    int result = nums[0];
    int left = 0;
    int right = numsSize - 1;

    while (left <= right) {
        if (nums[left] < nums[right]) {
            return result < nums[left] ? result : nums[left];
        }
        int middle = left + (right - left) / 2;
        result = result < nums[middle] ? result : nums[middle];
        if (nums[middle] >= nums[left]) {
            left = ++middle;
        } else {
            right = --middle;
        }
    }
    return result;
}

// Binary Search Solution (Lower Bound Approach
// Complexities:
// Time : O(logn)
// Space: O(1)
int findMin(int* nums, int numsSize) {
    int left = 0;
    int right = numsSize - 1;

    while (left < right) {
        int middle = left + (right - left) / 2;
        if (nums[middle] < nums[right]) {
            right = middle;
        } else {
            left = ++middle;
        }
    }
    return nums[left];
}
