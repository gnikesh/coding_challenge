# Given a binary tree struct TreeLinkNode { TreeLinkNode *left; TreeLinkNode *right; TreeLinkNode *next; } Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. Initially, all next pointers are set to NULL. Note: You may only use constant extra space. You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children). For example, Given the following perfect binary tree, 1 /  \ 2    3 / \  / \ 4  5  6  7 After calling your function, the tree should look like: 1 -> NULL /  \ 2 -> 3 -> NULL / \  / \ 4->5->6->7 -> NULL


# Definition for a TreeLinkNode.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root):
        # Time complexity: O(N) where N is the number of nodes in the tree, Space complexity: O(1)
        if not root:
            return
        level_start = root
        while level_start.left:
            node = level_start
            while node:
                # Set next pointer of left child
                node.left.next = node.right
                # If node has a next node, set next pointer of right child
                if node.next:
                    node.right.next = node.next.left
                # Move to next node
                node = node.next
            # Move to next level
            level_start = level_start.left
