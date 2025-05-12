// LeetCode 0238 - Product of Array Except Self
// Medium - Arrays & Hashing
// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
// You must write an algorithm that runs in O(n) time and without using the division operation.
/**
 * Note: The returned array must be malloced, assume caller calls free().
*/

// Two Pointer, Single Pass Solution
// Complexities:
// Time : O(n) - technically O(2n) but we reduce to O(n)
// Space: O(1) - technically O(n)  if we consider the return array to be extra memory
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int *result = malloc(sizeof(int)* numsSize);
    for(int i=0;i<numsSize;result[i++]=1);
    *returnSize = numsSize;

    int prefix = 1, postfix = 1;

    for (int i = 1, j = numsSize - 2; i < numsSize; i++, j--) {
        prefix *= nums[--i];
        postfix *= nums[++j];

        result[++i] *= prefix;
        result[--j] *= postfix;
    }
    return result;
}
