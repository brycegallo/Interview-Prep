// LeetCode 0485 - Max Consecutive Ones
// Easy - Arrays & Hashing
// Given a binary array nums, return the maximum number of consecutive 1's in the array.

// Iterative Solution
// Complexities:
// Time : O(n)
// Space: O(1)
int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int current, result = current = 0;
    for (int i = 0; i < numsSize; i++) {
        current = nums[i] == 0 ? 0 : current + 1;
        result = current > result ? current : result;
    }
    return result;
}
