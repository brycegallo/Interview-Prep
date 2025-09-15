# LeetCode 0133 - Clone Graph
# Medium - Graphs
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional  # included in original template

# Depth-First Search Solution
# Complexities:
# Time : O(V + E) - V = vertices (nodes), E = edges between nodes
# Space: O(V)
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def clone_dfs(node):
            if node not in old_to_new:
                old_to_new[node] = copy = Node(node.val)
                for neighbor in node.neighbors:
                    copy.neighbors.append(clone_dfs(neighbor))
                return copy
            return old_to_new[node]

        return clone_dfs(node) if node else None
