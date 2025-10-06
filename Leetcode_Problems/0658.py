# LeetCode 0658 - Find K Closest Elements 
# Medium - Sliding Window
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
#     |a - x| < |b - x|, or
#     |a - x| == |b - x| and a < b

# Sliding Window Solution
# Complexities:
# Time : O(log(n-k) + k)
# Space: O(k) - for the output array
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            middle = left + (right - left) // 2
            if x - arr[middle] > arr[middle + k] - x:
                left = middle + 1
            else:
                right = middle
        return arr[left:left+k]
