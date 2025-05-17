# LeetCode 1299 - Replace Elements with Greatest Element on Right Side
# Easy - Arrays & Hashing
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.

# Iterative Solution
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in range(len(arr) -1, -1, -1):
            arr[i], greatest = greatest, max(greatest, arr[i])
        return arr
