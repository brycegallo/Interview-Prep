# LeetCode 0424 - Longest Repeating Character Replacement
# Medium - Sliding Window
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Sliding Window Solution with Hash-Map
# Complexities:
# Time : O(n) - O(26*n) reducing to O(n)
# Space: O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = result = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            if (right - left + 1) - max(count.values()) > k:
                count[s[left]], left = count[s[left]] - 1, left + 1
            result = max(result, right - left + 1)
        return result
