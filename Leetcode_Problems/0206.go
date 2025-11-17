// LeetCode 0206 - Reverse Linked List
// Easy - Linked List
// Given the head of a singly linked list, reverse the list, and return the reversed list.

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
func reverseList(head *ListNode) *ListNode {
    var previous *ListNode
    current := head

    for current != nil {
        temp := current.Next
        current.Next = previous
        previous = current
        current = temp
    }
    return previous
}
