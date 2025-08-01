# LeetCode 0102 - Binary Tree Level Order Traversal
# Medium - Trees
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative Breadth-First Search Solution
# Complexities:
# Time : O(n)
# Space: O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_length = len(queue)
            level = []
            for i in range(queue_length):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                result.append(level)
        return result
