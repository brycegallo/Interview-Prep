// LeetCode 0055 - Jump Game
// Greedy - Medium
// You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
// Return true if you can reach the last index, or false otherwise.

// Greedy Iterative Solution
// Complexities:
// Time : O(n)
// Space: O(1) 
bool canJump(int* nums, int numsSize) {
    int goal = numsSize - 1;
    for (int i = numsSize - 2; i >= 0; i--) {
        goal = nums[i] + i >= goal ? i : goal;
    }
    return goal == 0 ? true : false;
}
