# LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
# Medium - Trees
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Depth-First Search Solution
# Complexities:
# Time : O(n)
# Space: O(n) - for the recursion stack
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preI = self.inI = 0

        def dfs(limit):
            if self.preI >= len(preorder) or inorder[self.inI] == limit:
                self.inI = self.inI + 1 if self.preI < len(preorder) else self.inI
                return None
            root = TreeNode(preorder[self.preI])
            self.preI += 1
            root.left, root.right = dfs(root.val), dfs(limit)
            return root

        return dfs(float('inf'))
