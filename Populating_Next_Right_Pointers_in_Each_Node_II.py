# Follow up for problem "Populating Next Right Pointers in Each Node". What if the given tree could be any binary tree? Would your previous solution still work? Note: You may only use constant extra space. For example, Given the following binary tree, 1 /  \ 2    3 / \    \ 4   5    7 After calling your function, the tree should look like: 1 -> NULL /  \ 2 -> 3 -> NULL / \    \ 4-> 5 -> 7 -> NULL


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                # Set next for left child
                head.left.next = head.right
                
                # If head has a next node, set next for right child
                if head.next:
                    head.right.next = head.next.left
                
                # Move to next node
                head = head.next
            
            # Move down to the next level
            leftmost = leftmost.left
        
        return root

# Time complexity: O(N) where N is the number of nodes
# Space complexity: O(1) as we are using constant space
