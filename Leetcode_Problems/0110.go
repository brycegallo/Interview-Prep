// LeetCode 0110 - Balanced Binary Tree
// Easy - Trees
// Given a binary tree, determine if it is height-balanced.

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
func isBalanced(root *TreeNode) bool {
    return dfs(root).balanced
}

func abs(x int) int {
    if x < 0 { return -x }
    return x
}

type Result struct {
    balanced bool
    height int
}

func dfs(root *TreeNode) Result {
    if root == nil { return Result{true, 0} }
    left, right := dfs(root.Left), dfs(root.Right)
    balanced := left.balanced && right.balanced && abs(left.height - right.height) <= 1
    return Result{balanced, 1 + max(left.height, right.height)}
}
