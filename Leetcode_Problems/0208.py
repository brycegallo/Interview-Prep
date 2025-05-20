# LeetCode 0208 - Implement Trie (Prefix Tree)
# Medium - Tries
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#    Trie() Initializes the trie object.
#    void insert(String word) Inserts the string word into the trie.
#    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Solution with separate TrieNode class
# Complexities:
# Time : O(n) for each function call, where n is the length of the string
# Space: O(t) - where t is the total number of TrieNodes created in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]
        current.endOfWord = True

    def search(self, word: str) -> bool:
        current = self.root

        for character in word:
            if character not in current.children:
                return False
            current = current.children[character]
        return current.endOfWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for character in prefix:
            if character not in current.children:
                return False
            current = current.children[character]
        return True
