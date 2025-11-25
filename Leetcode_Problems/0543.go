// LeetCode 0543 - Diameter of Binary Tree
// Easy - Trees
// Given the root of a binary tree, return the length of the diameter of the tree.
// The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
// The length of a path between two nodes is represented by the number of edges between them.

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// Recursive Depth-First Search Solution
// Complexities:
// Time : O(n)
// Space: O(n) - O(log(n)) if tree is balanced, O(n) if degenerate
func diameterOfBinaryTree(root *TreeNode) int {
    result := 0
    var dfs func(*TreeNode) int
    dfs = func(root *TreeNode) int {
        if root == nil {
            return 0
        }
        left := dfs(root.Left)
        right := dfs(root.Right)
        result = max(result, left + right)

        return 1 + max(left, right)
    }
    dfs(root)
    return result
}
