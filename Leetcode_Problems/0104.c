// LeetCode 0104 - Maximum Depth of Binary Tree
// Easy - Trees
// Given the root of a binary tree, return its maximum depth.
// A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
*/

// Recursive Depth-First Search Solution
// Complexities:
// Time : O(n)
// Space: O(h) - best case (balanced tree) O(log n), worst case (degenerate tree) O(n)
int maxDepth(struct TreeNode* root) {
    if (root) {
        int root_left = maxDepth(root->left), root_right = maxDepth(root->right);
        return root_left > root_right ? ++root_left : ++root_right;
    }
    return 0;
}
