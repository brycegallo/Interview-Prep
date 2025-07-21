# LeetCode 0701 - Insert into a Binary Search Tree
# Medium - Trees
# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
#
# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative Solution
# Complexities:
# Time : O(h) - best case O(log n), worst case O(n)
# Space: O(1)
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        while current:
            previous = current
            if current.val < val:
                current = current.right
                previous.right = previous.right if current else TreeNode(val)
            else:
                current = current.left
                previous.left = previous.left if current else TreeNode(val)
        return root if root else TreeNode(val)

# Recursive Solution
# Complexities:
# Time : O(h) - best case O(log n), worst case O(n)
# Space: O(h) - same as Time
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if root.val < val:
                root.right = self.insertIntoBST(root.right, val)
            else:
                root.left = self.insertIntoBST(root.left, val)
        return root if root else TreeNode(val)
