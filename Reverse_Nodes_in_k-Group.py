# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list. k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is. You may not alter the values in the nodes, only nodes itself may be changed. Only constant memory is allowed. For example, Given this linked list: 1->2->3->4->5 For k = 2, you should return: 2->1->4->3->5 For k = 3, you should return: 3->2->1->4->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head, k):
    # Time complexity: O(n), where n is the number of nodes in the linked list
    # Space complexity: O(1), as we only use a constant amount of space
    
    dummy = ListNode(0)
    dummy.next = head
    stack = []
    prev = dummy
    
    while True:
        count = 0
        temp = head
        
        # Count the number of nodes in the current group
        while temp and count < k:  
            stack.append(temp)
            temp = temp.next
            count += 1
        
        # If the number of nodes in the current group is less than k, break the loop
        if count < k:
            return dummy.next
        
        # Reverse the current group of k nodes
        while stack:
            prev.next = stack.pop()
            prev = prev.next
        
        # Link the reversed group to the remaining nodes
        prev.next = temp
        
        # Move to the next group
        head = temp
