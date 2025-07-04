# LeetCode 0143 - Reorder List
# Medium - Linked List
# You are given the head of a singly linked-list. The list can be represented as:
#   L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#   L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Two-Pass Solution with No Extra Memory
# Complexities:
# Time : O(n)
# Space: O(1)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        
        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # split list and reverse second half
        second = slow.next
        previous = slow.next = None

        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp

        # merge halves of list into one again
        first, second = head, previous
        while second:
            temp_1 = first.next
            temp_2 = second.next
            first.next = second
            second.next = temp_1
            first, second = temp_1, temp_2
