# LeetCode 0042 - Trapping Rain Water
# Hard - Two Pointers
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Single Pass, Two-Pointer Solution
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        result, left, right = 0, 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while height and left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
            # because left_max or right_max will be changed conditionally above, the below line may not execute as intended
            result += (left_max - height[left]) if left_max < right_max else (right_max - height[right])
        return result

