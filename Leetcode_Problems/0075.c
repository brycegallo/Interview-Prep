// LeetCode 0075 - Sort Colors
// Medium - Arrays & Hashing
// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

// We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
//
// You must solve this problem without using the library's sort function.

// One Pass Two-Pointer Solution
// Complexities:
// Time : O(n)
// Space: O(1)
void sortColors(int* nums, int numsSize) {
    int left, temp = left = 0;
    int right = numsSize - 1;
    
    for (int index = 0; index <= right; index++) {
        temp = nums[index] == 1 ? nums[index] : nums[index] == 2 ? nums[right] : nums[left];
        if (nums[index] == 0) {
            nums[left++] = nums[index];
            nums[index] = temp;
        }
        else if (nums[index] == 2) {
            nums[right--] = nums[index];
            nums[index--] = temp;
        }
    }
}
