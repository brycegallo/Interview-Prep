# LeetCode 0098 - Validate Binary Search Tree
# Medium - Trees
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
#    The left subtree of a node contains only nodes with values less than the node's value.
# The right subtree of a node contains only nodes with values greater than the node's value.
# Both the left and right subtrees must also be binary search trees.

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l_bound, u_bound):
            if node and (l_bound < node.val < u_bound):
                return dfs(node.left, l_bound, node.val) and dfs(node.right, node.val, u_bound)
            return False if node else True
        return dfs(root, -(inf), inf)
