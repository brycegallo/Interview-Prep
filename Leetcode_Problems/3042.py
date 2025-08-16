# LeetCode 3042 - Count Prefix and Suffix Pairs I
# Easy - Tries
# You are given a 0-indexed string array words.
# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
#     isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix  and a suffix of str2, and false otherwise.
# For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.
# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

# Brute Force Solution
# Complexities:
# Time : O(n^2)
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                w_1, w_2, w_1_len = words[i], words[j], len(words[i])
                if w_1 == w_2[:w_1_len] and words[i] == w_2[-w_1_len:]:
                    result += 1
        return result

