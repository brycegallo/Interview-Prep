# LeetCode 0427 - Construct Quad Tree
# Medium - Trees
# Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.
# Return the root of the Quad-Tree representing grid.
# A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:
#     val: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.
#     isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
# We can construct a Quad-Tree from a two-dimensional area using the following steps:
#     If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and set the four children to Null and stop.
#     If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into four sub-grids as shown in the photo.
#     Recurse for each of the children with the proper sub-grid.
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
# Recursive Solution
# Complexities:
# Time : O(n^2 * logn)
# Space: O(logn)
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, row, col):
            all_same = True
            for i in range(n):
                for j in range(n):
                    if grid[row][col] != grid[row + i][col + j]:
                        all_same = False
                        break
            if all_same:
                return Node(grid[row][col], True)
            n = n // 2
            top_left = dfs(n, row, col)
            top_right = dfs(n, row, col + n)
            bottom_left = dfs(n, row + n, col)
            bottom_right = dfs(n, row + n, col + n)
            return Node(0, False, top_left, top_right, bottom_left, bottom_right)
        return dfs(len(grid), 0, 0)
