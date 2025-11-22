// LeetCode 0226 - Invert Binary Tree
// Medium - Trees
// Given the root of a binary tree, invert the tree, and return its root.

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// Iterative Depth-First Search Solution
// Complexities:
// Time : O(n)
// Space: O(n)
func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    root.Left, root.Right = root.Right, root.Left

    invertTree(root.Left)
    invertTree(root.Right)
    return root
}
