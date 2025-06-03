// LeetCode 0011 - Container with Most Water
// Medium - Two Pointers
// You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
// Find two lines that together with the x-axis form a container, such that the container contains the most water.
// Return the maximum amount of water a container can store.
// Notice that you may not slant the container.

// Single-Pass, Two-Pointer, Greedy Solution
// Complexities:
// Time : O(n)
// Space: O(1)
int maxArea(int* height, int heightSize) {
    int max_area = 0;
    int left = 0;
    int right = heightSize - 1;

    while (left < right) {
        int current_lowest = height[left] < height[right] ? height[left] : height[right];
        int current_area = (right - left) * current_lowest;
        max_area = max_area < current_area ? current_area : max_area;

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return max_area;
}
