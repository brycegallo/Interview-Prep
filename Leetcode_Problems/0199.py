# LeetCode 0199 - Binary Tree Right Side View 
# Medium - Trees
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

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
                result.append(level[-1])
        return result
