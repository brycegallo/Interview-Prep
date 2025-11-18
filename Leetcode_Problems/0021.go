// LeetCode 0021 - Merge Two Sorted Lists
// Easy - Linked List
// You are given the heads of two sorted linked lists list1 and list2.
// Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
// Return the head of the merged linked list.

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// Solution
// Complexities:
// Time : O(m + n)
// Space: O(1)
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    placeholder := &ListNode{}
    node := placeholder

    for list1 != nil && list2 != nil {
        if list1.Val < list2.Val {
            node.Next = list1
            list1 = list1.Next
        } else {
            node.Next = list2
            list2 = list2.Next
        }
        node = node.Next
    }
    node.Next = list1
    if list1 == nil {
        node.Next = list2
    }
    return placeholder.Next
}
