# Given a binary tree, find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
    # Time complexity: O(n), where n is the number of nodes in the tree
    # Space complexity: O(h), where h is the height of the tree
    if root is None:
        return 0
    else:
        left_height = maxDepth(root.left)
        right_height = maxDepth(root.right)
        return max(left_height, right_height) + 1

# Example usage:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(maxDepth(root))  # Output: 3
