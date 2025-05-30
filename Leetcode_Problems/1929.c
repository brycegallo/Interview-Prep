// LeetCode 1929 - Concatenation of Array
// Easy - Arrays & Hashing
// Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
// Specifically, ans is the concatenation of two nums arrays.
// Return the array ans.
//
/**
 * Note: The returned array must be malloced, assume caller calls free().
*/

// Single-Pass Solution
// Complexities: 
// Time : O(n)
// Space: O(n)
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize * 2;
    int* ans = malloc(sizeof(int) * numsSize * 2);
    
    for (int i = 0; i < numsSize; i++) {
        //int second_i = i + numsSize;
        //ans[i] = nums[i];
        //ans[second_i] = ans[i];
	// commented lines above are expressed more succinctly in line below
        ans[i] = ans[(i + numsSize)] = nums[i];
    }
    return ans;
}
