# LeetCode 0124 - Binary Tree Maximum Path Sum
# Hard - Trees
# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Depth-First Solution with Global Variable
# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        def dfs(root):
            if root:
                left_max, right_max = max(dfs(root.left), 0), max(dfs(root.right), 0)
                # compute max path sum with splitting
                self.result = max(self.result, root.val + left_max + right_max)
                # return max path sum without splitting
                return root.val + max(left_max, right_max, 0)
            return 0

        dfs(root)
        return self.result

