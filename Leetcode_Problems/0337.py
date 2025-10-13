# LeetCode 0337 - House Robber III
# Medium - Trees
# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
# Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.
# Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # return pair: [with_root, without_root]
        def dfs(root):
            if root:
                left_pair, right_pair = dfs(root.left), dfs(root.right)

                with_root = root.val + left_pair[1] + right_pair[1]
                without_root = max(left_pair) + max(right_pair)
            return [0, 0] if not root else [with_root, without_root]
        return max(dfs(root))
