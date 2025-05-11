// LeetCode 0169 - Majority Element
// Easy - Hashing & Arrays
// Given an array nums of size n, return the majority element.
// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array. 

// Sorting and Iterative Solution
// Complexities:
// Time : O(n * logn)
// Space: O(1)
int compare(const void* a, const void* b) {
    int* int_a = a;
    int* int_b = b;
    return *int_a - *int_b;
}

int majorityElement(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(nums[0]), compare);
    int half = (numsSize / 2);

    int i = 0;
    int count = 1;
    while (i < numsSize - 1) {
        if (nums[i+1] == nums[i++]) {
            if (++count > half) {
                break;
            }
            continue;
        }
        count = 1;
    }
    return nums[i];
}

// Sorting and Solution without iteration
// Complexities:
// Time : O(logn)
// Space: O(1)
int compare(const void* a, const void* b) {
    int* int_a = a;
    int* int_b = b;
    return *int_a - *int_b;
}

int altMajorityElement(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(nums[0]), compare);
    return [numsSize / 2];
}
