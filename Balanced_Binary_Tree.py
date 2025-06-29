# Given a binary tree, determine if it is height-balanced. For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root):
            # Base case
            if not root:
                return 0
            # Recursively check left and right subtrees
            left = check(root.left)
            right = check(root.right)
            # If left or right subtree is not balanced, return -1
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            # Return the height of the tree
            return 1 + max(left, right)
        
        return check(root) != -1

# Time complexity: O(N) where N is the number of nodes in the tree
# Space complexity: O(H) where H is the height of the tree
