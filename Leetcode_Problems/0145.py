# LeetCode 0145 - Binary Tree Postorder Traversal
# Easy - Trees
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative Depth-First Search Solution
# Complexities:
# Time : O(n)
# Space: O(n) - O(n) each for the stacks and output array, O(2n) reducing to O(n)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visit = [False]
        result = []

        while stack:
            current, v = stack.pop(), visit.pop()
            if current:
                if v:
                    result.append(current.val)
                else:
                    stack.append(current)
                    visit.append(True)
                    stack.append(current.right)
                    visit.append(False)
                    stack.append(current.left)
                    visit.append(False)

        return result
