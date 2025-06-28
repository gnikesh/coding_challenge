# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Base case
        if not head:
            return None
        
        # Time complexity: O(1) for finding the middle node
        # Space complexity: O(1) for the recursive call stack
        if not head.next:
            return TreeNode(head.val)
        
        # Find the middle node
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Break the linked list at the middle node
        prev.next = None
        
        # Recursive call to construct the left and right subtrees
        # Time complexity: O(N) for traversing the linked list
        # Space complexity: O(log N) for the recursive call stack
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        
        return node

# Time complexity: O(N) for traversing the linked list
# Space complexity: O(log N) for the recursive call stack
