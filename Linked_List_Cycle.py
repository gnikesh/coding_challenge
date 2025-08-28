# Given a linked list, determine if it has a cycle in it. Follow up: Can you solve it without using extra space?


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    # Initialize two pointers, one moving twice as fast as the other
    slow = head
    fast = head
    
    # Traverse the linked list
    while fast is not None and fast.next is not None:
        # Move the slow pointer one step at a time
        slow = slow.next
        # Move the fast pointer two steps at a time
        fast = fast.next.next
        
        # If there is a cycle, the fast pointer will eventually catch up to the slow pointer
        if slow == fast:
            return True
    
    # If the fast pointer reaches the end of the linked list, there is no cycle
    return False

# Time complexity: O(n), where n is the number of nodes in the linked list
# Space complexity: O(1), as we only use a constant amount of space to store the slow and fast pointers
