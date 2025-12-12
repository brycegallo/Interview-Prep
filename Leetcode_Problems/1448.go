// LeetCode 1448 - Count Good Nodes in Binary Tree
// Medium - Trees
// Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
// Return the number of good nodes in the binary tree.

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
func goodNodes(root *TreeNode) int {
    var dfs func(node *TreeNode, max_val int) int
    dfs = func(node *TreeNode, max_val int) int {
        if node == nil { return 0}

        result := 0
        if node.Val >= max_val { result = 1 }

        max_val = max(max_val, node.Val)
        result += dfs(node.Left, max_val) + dfs(node.Right, max_val)

        return result
    }
    return dfs(root, root.Val)
}
