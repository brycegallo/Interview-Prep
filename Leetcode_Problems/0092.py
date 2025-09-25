# LeetCode 0092 - Reverse Linked List II
# Medium - Linked List
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative Solution with Placeholder Node
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        placeholder = ListNode(0, head)
        
        # Phase 1: reach node at position "left"
        left_prev, curr = placeholder, head
        for i in range(left - 1):
            left_prev, curr = curr, curr.next

        # Phase 2: reverse from left to right
        prev = None
        for i in range(right - left + 1):
            temp_next = curr.next
            curr.next = prev
            prev, curr = curr, temp_next

        # Phase 3: update and clean up pointers
        left_prev.next.next = curr  # curr is the node after "right"
        left_prev.next = prev  # prev is "right"
        return placeholder.next
