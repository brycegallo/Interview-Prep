// LeetCode 0235 - Lowest Common Ancestor of a Binary Search Tree
// Medium - Trees
// Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
// According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// Iterative Solution
// Complexities:
// Time : O(h) - h is the height of the tree
// Space: O(1)

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    while (root != NULL) {
        if (p->val > root->val && q->val > root->val) { root = root->right; }
        else if (p->val < root->val && q->val < root->val) { root = root->left; }
        else { break; }
    }
    return root;
}
