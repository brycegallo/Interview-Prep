# LeetCode 1448 - Count Good Nodes in Binary Tree
# Medium - Trees
# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Depth-First Search Solution
# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_value):
            if node:
                result = 1 if node.val >= max_value else 0
                max_value = max(node.val, max_value)
                result += dfs(node.left, max_value) + dfs(node.right, max_value)
            return result if node else 0

        return dfs(root, root.val)

