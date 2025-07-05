# Given a binary tree, flatten it to a linked list in-place. For example, Given 1 / \ 2   5 / \   \ 3   4   6 The flattened tree should look like: 1 \ 2 \ 3 \ 4 \ 5 \ 6 click to show hints. Hints: If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # Recursively call for left and right subtree
        self.flatten(root.left)
        self.flatten(root.right)
        
        # If left child is not None, move it to the right
        if root.left:
            # Store the right child
            right_child = root.right
            
            # Move left child to the right
            root.right = root.left
            root.left = None
            
            # Find the rightmost node of the left child
            rightmost = root.right
            while rightmost.right:
                rightmost = rightmost.right
            
            # Set the rightmost node's right child to the original right child
            rightmost.right = right_child

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(h), where h is the height of the tree due to recursion stack
