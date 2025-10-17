# LeetCode 2807 - Insert Greatest Common Divisors in Linked List
# Medium - Math & Geometry
# Given the head of a linked list head, in which each node contains an integer value.
# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
# Return the linked list after insertion.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution
# Complexities:
# Time : O(m * log(min(n))) - m is the number of nodes, n is the largest node passed to gcd()
# Space: O(1)
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(num_1, num_2):
            while num_2 > 0:
                num_1, num_2 = num_2, num_1 % num_2
            return num_1
        
        current = head
        while current.next:
            node_1, node_2 = current.val, current.next.val
            current.next = ListNode(gcd(node_1, node_2), current.next)
            current = current.next.next
        return head
