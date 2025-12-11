// LeetCode 0199 - Binary Tree Right Side View
// Medium - Trees
// Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

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
// Space: O(n)
func rightSideView(root *TreeNode) []int {
    var result []int

    var dfs func(node *TreeNode, depth int)
    dfs = func(node *TreeNode, depth int) {
        if node == nil { return }
        if depth == len(result) { result = append(result, node.Val) }
        dfs(node.Right, depth+1)
        dfs(node.Left, depth+1)
    }
    dfs(root, 0)
    return result
}
