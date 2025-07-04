# LeetCode 0019 - Remove Nth Node from End of List
# Medium - Linked List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Single Pass Solution with Placeholder Node
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        placeholder = ListNode(0, head)
        left, right = placeholder, head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left, right = left.next, right.next

        left.next = left.next.next
        return placeholder.next
