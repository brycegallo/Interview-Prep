# LeetCode 0011 - Container with Most Water
# Medium - Two Pointers
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Single-Pass, Two-Pointer, Greedy Solution
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            lower_height = min(height[left], height[right])
            current_area = (right - left) * lower_height
            max_area = max(max_area, current_area)

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return max_area
