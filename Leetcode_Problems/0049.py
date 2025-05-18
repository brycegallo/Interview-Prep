# LeetCode 0049 - Group Anagrams
# Medium - Arrays & Hashing
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Iterative Hashing Solution
# Complexities:
# Time : O(m * n * 26) - reduces to O(m * n)
# Space: O(m * n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(word)
        return list(result.values())
