// LeetCode 0876 - Middle of the Linked List
// Easy - Linked List
// Given the head of a singly linked list, return the middle node of the linked list.
// If there are two middle nodes, return the second middle node.
//
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
*/

// Iterative Two Pointer Solution
// Complexities:
// Time : O(n)
// Space: O(1)
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode* tortoise = head;
    struct ListNode* hare = head;
    while (hare != NULL && hare->next != NULL) {
        hare = hare->next->next;
        tortoise = tortoise->next;
    }
    return tortoise;
}
