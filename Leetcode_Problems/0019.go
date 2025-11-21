// LeetCode 0019 - Remove Nth Node From End of List
// Medium - Linked List
// Given the head of a linked list, remove the nth node from the end of the list and return its head.

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// Solution
// Complexities:
// Time : O(n)
// Space: O(1)
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    placeholder := &ListNode{Next: head}
    left, right := placeholder, head

    for n > 0 {
        right, n = right.Next, n - 1
    }

    for right != nil {
        left, right = left.Next, right.Next
    }

    left.Next = left.Next.Next
    return placeholder.Next
}
