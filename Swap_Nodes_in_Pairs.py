# Given a linked list, swap every two adjacent nodes and return its head. For example, Given 1->2->3->4, you should return the list as 2->1->4->3. Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Create a dummy node to simplify some corner cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # O(1) space

        # Time complexity : O(n) where n is the number of nodes in the linked list
        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next

            # Swapping
            prev.next = second_node  # 
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev for next swap
            prev = first_node
            head = first_node.next

        # Space complexity : O(1)
        return dummy.next
