# Given a list, rotate the list to the right by k places, where k is non-negative. For example: Given 1->2->3->4->5->NULL and k = 2, return 4->5->1->2->3->NULL.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        
        # Close the linked list into a ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        
        old_tail.next = head
        
        # Find the new tail node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        
        # Find the new head node
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head

# Time complexity: O(L) where L is the length of the linked list
# Space complexity: O(1) as a constant amount of space is used
