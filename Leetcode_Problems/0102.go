// LeetCode 0102 - Binary Tree Level Order Traversal
// Medium - Trees
// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// Breadth-First Search Solution
// Complexities:
// Time : O(n)
// Space: O(n)
func levelOrder(root *TreeNode) [][]int {
    result := [][]int{}
    if root == nil { return result }

    queue := []*TreeNode{root}

    for len(queue) > 0 {
        queue_length := len(queue)
        level := []int{}
        
        for i := 0; i < queue_length; i++ {
            node := queue[0]
            queue = queue[1:]
            level = append(level, node.Val)
            if node.Left != nil { queue = append(queue, node.Left)}
            if node.Right != nil { queue = append(queue, node.Right)}
        }
        result = append(result, level)
    }
    return result
}
