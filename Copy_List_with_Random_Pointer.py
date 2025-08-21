# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null. Return a deep copy of the list.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        # Create a dictionary to store the nodes we have seen
        node_dict = {}

        # Create a new node for each node in the original list
        current = head
        while current:
            node_dict[current] = Node(current.val)
            current = current.next

        # Set the next and random pointers for each new node
        current = head
        while current:
            if current.next:
                node_dict[current].next = node_dict[current.next]
            if current.random:
                node_dict[current].random = node_dict[current.random]
            current = current.next

        # Time complexity: O(n), where n is the number of nodes in the list
        # Space complexity: O(n), where n is the number of nodes in the list
        return node_dict[head]
