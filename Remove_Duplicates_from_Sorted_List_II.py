# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. For example, Given 1->2->3->3->4->4->5, return 1->2->5. Given 1->1->1->2->3, return 2->3.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        
        # Traverse the list
        while cur:
            # If it's not a duplicate node
            if cur.next and cur.val != cur.next.val:
                pre = pre.next
                cur = cur.next
            # If it's a duplicate node
            else:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                # Remove all the duplicate nodes
                pre.next = cur.next
                cur = cur.next
        
        return dummy.next
    
# Time complexity: O(n), where n is the number of nodes in the list.
# Space complexity: O(1), as we are just using a constant amount of space.
