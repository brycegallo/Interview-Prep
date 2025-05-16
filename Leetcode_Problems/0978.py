# LeetCode 0978 - Longest Turbulent Subarray
# Medium - Greedy
# Given an integer array arr, return the length of a maximum size turbulent subarray of arr. A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
#
# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
# For i <= k < j:
#   arr[k] > arr[k + 1] when k is odd, and
#   arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
#   arr[k] > arr[k + 1] when k is even, and
#   arr[k] < arr[k + 1] when k is odd.

# Two Pointer Solution
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right, result, previous = 0, 1, 1, ""

        while right < len(arr):
            if arr[right - 1] > arr[right] and previous != ">":
                result = max(result, right - left + 1)
                right += 1
                previous = ">"
            elif arr[right - 1] < arr[right] and previous != "<":
                result = max(result, right - left + 1)
                right += 1
                previous = "<"
            else:
                right = right + 1 if arr[right] == arr[right - 1] else right
                left = right - 1
                previous = ""
        return result
