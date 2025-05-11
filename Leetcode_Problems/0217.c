// leetcode 0217: contains duplicate
// Easy - Arrays & Hashing
// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

// Brute force, passes 65/77 testcases on leetcode, fails 66th due to limit exceeded
// Complexities:
// Time : O(n^2)
// Space: O(1)
bool containsDuplicate(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
	for (int j = i + 1; j < numsSize; j++) {
	    if (nums[i] == nums[j]) {
		return true;
	    }
	}
    }
    return false;
}

// Sort with qsort() - almost optimal, should use hashing for better optimization
// Complexities:
// Time : O(n * logn)
// Space: O(1)
int compare (const void *a, const void *b) {
    int *value_a = a;
    int *value_b = b;
    return *value_a - *value_b;
}

bool containsDuplicate(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(nums[0]), compare);
    for (int i = 0; i < numsSize - 1; i++) {
	if (nums[i] == nums[i + 1]) {
	    return true;
	}
    }
    return false;
}
