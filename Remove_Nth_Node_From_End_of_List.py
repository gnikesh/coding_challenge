# Given a linked list, remove the nth node from the end of list and return its head. For example, Given linked list: 1->2->3->4->5, and n = 2. After removing the second node from the end, the linked list becomes 1->2->3->5. Note: Given n will always be valid. Try to do this in one pass.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # Initialize two pointers with same node (head)
    # one pointer (A) will be always n steps ahead of second pointer (B)
    A, B = head, head
    # move A n steps ahead
    for _ in range(n):
        A = A.next
    
    # move both pointers one step at a time
    if not A:
        # this means we need to remove head
        return head.next
    
    while A.next:
        A = A.next
        B = B.next
    
    # Remove nth node from end
    B.next = B.next.next
    
    # Return the head of the changed list
    return head
# Time Complexity: O(length_of_list)
# Space Complexity: O(1)
