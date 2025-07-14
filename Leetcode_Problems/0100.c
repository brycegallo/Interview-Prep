// LeetCode 0100 - Same Tree
// Easy - Trees
// Given the roots of two binary trees p and q, write a function to check if they are the same or not.
// Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

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
// Space: O(1)
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    if (!p && !q) return true;
    if (!p || !q || p->val != q->val) return false;
    return (isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
}
