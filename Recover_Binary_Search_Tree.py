# Two elements of a binary search tree (BST) are swapped by mistake. Recover the tree without changing its structure. Note: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.first = None
        self.second = None
        self.prev = None
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        if self.prev and self.prev.val > root.val:
            if self.first is None:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.inorder(root.right)

# Time complexity: O(n), where n is the number of nodes in the tree
# Space complexity: O(h), where h is the height of the tree (O(1) for balanced binary search tree, O(n) for skewed tree)
