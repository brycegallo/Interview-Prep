// LeetCode 0287 - Find the Duplicate Number
// Medium - Linked List
// Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
//
// There is only one repeated number in nums, return this repeated number.
//
// You must solve the problem without modifying the array nums and using only constant extra space.

// Floyd's Algorith Solution (Tortoise and Hare)
// Complexities:
// Time : O(n)
// Space: O(1)
int findDuplicate(int* nums, int numsSize) {
    int slow_1 = nums[0], slow_2 = 0, fast = nums[nums[0]];

    while (slow_1 != fast)   { slow_1 = nums[slow_1], fast = nums[nums[fast]]; }
    while (slow_1 != slow_2) { slow_1 = nums[slow_1], slow_2 = nums[slow_2];   }
    return slow_1;
}
