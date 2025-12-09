// LeetCode 0235 - Lowest Common Ancestor of a Binary Search Tree
// Medium - Trees
// Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
// According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// Iterative Solution
// Complexities:
// Time : O(h) - h is the height of the tree
// Space: O(1)
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	for root != nil {
        if min(p.Val, q.Val) > root.Val {
            root = root.Right
        } else if max(p.Val, q.Val) < root.Val {
            root = root.Left
        } else { break }
    }
    return root
}
