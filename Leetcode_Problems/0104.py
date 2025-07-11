# LeetCode 0104 - Maximum Depth of Binary Tree
# Easy - Trees
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Depth-First Search Solution
# Complexities:
# Time : O(n)
# Space: O(h) - best case (balanced tree) O(log n), worst case (degenerate tree) O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
