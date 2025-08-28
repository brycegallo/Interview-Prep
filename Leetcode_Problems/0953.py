# LeetCode 0953 - Verifying an Alien Dictionary
# Easy - Graphs
# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

# Iterative HashMap Solution
# Complexities:
# Time : O(m * n) - m is the number of words and n is the average length of the words
# Space: O(1) - O(26) for the 26 different possible characters
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {char: index for index, char in enumerate(order)}

        for i in range(len(words) - 1):
            word_1, word_2 = words[i], words[i + 1]

            for j in range(len(word_1)):
                if j == len(word_2):
                    return False
                if word_1[j] != word_2[j]:
                    if order_index[word_2[j]] < order_index[word_1[j]]:
                        return False
                    break

        return True

