# LeetCode 0110 - Balanced Binary Tree
# Easy - Trees
# Given a binary tree, determine if it is height-balanced

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Depth-First Search Solution
# Complexities:
# Time : O(n)
# Space: O(n) - Best Case O(log n) = O(h) if tree is balanced, worst case O(n) if not balanced at all
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(root):
            if root:
                left, right = 1 + dfs(root.left), 1 + dfs(root.right)
                self.balanced = False if abs(left - right) > 1 else self.balanced
            return 0 if not root else max(left, right)

        dfs(root)
        return self.balanced
