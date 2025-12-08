// LeetCode 0572 - Subtree of Another Tree
// Easy - Trees
// Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
// A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

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
// Time : O(m * n)
// Space: O(m + n)
func helperSameTree(root *TreeNode, subRoot * TreeNode) bool {
    if root == nil && subRoot == nil { return true }
    if root != nil && subRoot != nil && root.Val == subRoot.Val {
        return helperSameTree(root.Left, subRoot.Left) && helperSameTree(root.Right, subRoot.Right)
    }
    return false
}

func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
    if subRoot == nil { return true }
    if root == nil { return false }
    if helperSameTree(root, subRoot) { return true }
    return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
}
