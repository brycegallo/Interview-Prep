// LeetCode 0042 - Trapping Rain Water
// Hard - Two Pointers
// Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

// Single Pass, Two-Pointer Solution
// Complexities:
// Time : O(n)
// Space: O(1)
int trap(int* height, int heightSize) {
    int result = 0;
    int left = 0;
    int right = heightSize - 1;
    int left_max = height[left];
    int right_max = height[right];

    while (heightSize > 0 && left < right) {
        if (left_max < right_max) {
            left_max = left_max > height[++left] ? left_max : height[left];
        } else {
            right_max = right_max > height[--right] ? right_max : height[right];
        }
	// because left_max or right_max will be changed conditionally above, the below line may not execute as intended
        result += left_max < right_max ? (left_max - height[left]) : (right_max - height[right]);
    }
    return result;
}
