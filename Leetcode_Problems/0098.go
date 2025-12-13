// LeetCode 0098 - Validate Binary Search Tree
// Medium - Trees
// Given the root of a binary tree, determine if it is a valid binary search tree (BST).
// A valid BST is defined as follows:
//     The left subtreeof a node contains only nodes with keys strictly less than the node's key.
//     The right subtree of a node contains only nodes with keys strictly greater than the node's key.
//     Both the left and right subtrees must also be binary search trees.

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
func isValidNode(node *TreeNode, left, right int64) bool {
    if node == nil { return true }
    val := int64(node.Val)
    if val <= left || val >= right { return false }
    return isValidNode(node.Left, left, val) && isValidNode(node.Right, val, right)
}

func isValidBST(root *TreeNode) bool {
    return isValidNode(root, math.MinInt64, math.MaxInt64)
}
