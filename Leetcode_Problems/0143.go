// LeetCode 0143 - Reorder List
// Medium - Linked List
// You are given the head of a singly linked-list. The list can be represented as:
// L0 → L1 → … → Ln - 1 → Ln
// Reorder the list to be on the following form:
// L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
// You may not modify the values in the list's nodes. Only nodes themselves may be changed.

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
func reorderList(head *ListNode)  {
    if head == nil || head.Next == nil {
        return
    }
    
    slow, fast := head, head.Next
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }

    second := slow.Next
    slow.Next = nil
    var previous *ListNode
    for second != nil {
        temp := second.Next
        second.Next = previous
        previous = second
        second = temp
    }

    first := head
    second = previous
    for second != nil {
        temp_1, temp_2 := first.Next, second.Next
        first.Next = second
        second.Next = temp_1
        first, second = temp_1, temp_2
    }
}
