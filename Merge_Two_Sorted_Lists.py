# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        # Time complexity: O(n + m) 
        # Space complexity: O(n + m)
        """ 
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        current_node = dummy_node
        
        while l1 and l2:
            # Select the smaller node from l1 and l2 to append to current_node
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next
        
        # Append the remaining nodes from l1 or l2
        if l1:
            current_node.next = l1
        elif l2:
            current_node.next = l2
        
        return dummy_node.next

