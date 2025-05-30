# Given a binary tree, return the inorder traversal of its nodes' values. For example: Given binary tree [1,null,2,3], 1 \ 2 / 3 return [1,3,2]. Note: Recursive solution is trivial, could you do it iteratively?


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def inorderTraversal(root):
    # Time complexity: O(n), where n is the number of nodes in the tree
    # Space complexity: O(n), where n is the number of nodes in the tree
    result = []
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            break
        node = stack.pop()
        result.append(node.val)
        root = node.right
    return result

def inorderTraversalRecursive(root):
    # Time complexity: O(n), where n is the number of nodes in the tree
    # Space complexity: O(n), where n is the number of nodes in the tree in the worst case (when tree is skewed)
    def traversal(node):
        if node:
            traversal(node.left)
            result.append(node.val)
            traversal(node.right)
    result = []
    traversal(root)
    return result

# Example usage:
# Create a binary tree: [1,null,2,3]
#       1
#        \
#         2
#        /
#       3
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(inorderTraversal(root))  # Output: [1, 3, 2]
print(inorderTraversalRecursive(root))  # Output: [1, 3, 2]
