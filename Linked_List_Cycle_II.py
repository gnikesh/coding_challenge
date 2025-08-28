# Given a linked list, return the node where the cycle begins. If there is no cycle, return null. Note: Do not modify the linked list. Follow up: Can you solve it without using extra space?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Time complexity: O(n), where n is the number of nodes in the linked list.
        # Space complexity: O(1), as we are not using any extra space.
        
        # Phase 1: Detecting the cycle using Floyd's Tortoise and Hare algorithm
        tortoise = head
        hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                break
        
        # If there is no cycle, return None
        if not hare or not hare.next:
            return None
        
        # Phase 2: Finding the start of the cycle
        tortoise = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
        
        return tortoise

def main():
    # Create a linked list with a cycle
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Create a cycle
    
    solution = Solution()
    cycle_start = solution.detectCycle(node1)
    
    if cycle_start:
        print(cycle_start.val)  # Output: 2
    else:
        print("No cycle found")

if __name__ == "__main__":
    main()
