# LeetCode 0543 - Diameter of Binary Tree
# Easy - Trees
# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Depth-First Search Solution
# Complexities:
# Time : O(n)
# Space: O(n) - Best case O(h) = O(log n) if tree is balanced, worst case O(n) if tree is not balanced
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(root):
            if root:
                left, right = dfs(root.left), dfs(root.right)
                self.result = max(self.result, left + right)
            return 0 if not root else 1 + max(left, right)
        dfs(root)
        return self.result
