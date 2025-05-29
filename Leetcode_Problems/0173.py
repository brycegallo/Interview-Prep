# LeetCode 0173 - Binary Search Tree Iterator
# Medium - Trees
# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
#    BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
#    boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
#    int next() Moves the pointer to the right, then returns the number at the pointer.
#
# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
#
# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        current = root
        while current:
            self.stack.append(current)
            current = current.left

    def next(self) -> int:
        result = self.stack.pop()
        current = result.right
        while current:
            self.stack.append(current)
            current = current.left
        return result.val

    def hasNext(self) -> bool:
        return self.stack != []
