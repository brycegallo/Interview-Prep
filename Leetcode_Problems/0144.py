# LeetCode 0144 - Binary Tree Preorder Traversal
# Easy - Trees
# Given the root of a binary tree, return the preorder traversal of its nodes' values.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative Depth-First Search Solution
# Complexities:
# Time : O(n)
# Sapce: O(n) - O(n) for the stack and O(n) for the output array, so O(2n) reducing to O(n)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        current = root
        stack, result = [], []
        while current or stack:
            if current:
                result.append(current.val)
                stack.append(current.right)
                current = current.left
            else:
                current = stack.pop()

        return result
