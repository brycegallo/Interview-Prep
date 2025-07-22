# LeetCode 0450 - Delete Node in a BST
# Medium - Trees
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
#    Search for a node to remove.
#    If the node is found, delete the node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Solution
# Complexities:
# Time : O(h) - O(log n) best case scenario, O(n) worst case
# Space: O(h) - same as Time
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            elif root.val > key:
                root.left = self.deleteNode(root.left, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                current = root.right
                while current.left:
                    current = current.left
                root.val = current.val
                root.right = self.deleteNode(root.right, root.val)
        return root
