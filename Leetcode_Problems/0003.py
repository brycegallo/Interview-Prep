# Leetcode 0003 - Longest Substring Without Repeating Characters
# Easy - Arrays & Hashing
# Given a string s, find the length of the longest substring without duplicate characters.

# Sliding Window Solution
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        length = len(s)
        max_count = count = left = right = 0

        while right < length:
            if s[right] not in window:
                window.add(s[right])
                count += 1
                max_count = max(count, max_count)
                right += 1
            else:
                window.remove(s[left])
                count -= 1
                left += 1
        return max_count
