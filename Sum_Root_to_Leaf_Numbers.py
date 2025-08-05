# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number. An example is the root-to-leaf path 1->2->3 which represents the number 123. Find the total sum of all root-to-leaf numbers. For example, 1 / \ 2   3 The root-to-leaf path 1->2 represents the number 12. The root-to-leaf path 1->3 represents the number 13. Return the sum = 12 + 13 = 25.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sumNumbers(root):
    # Time complexity: O(N) where N is the number of nodes in the tree
    # Space complexity: O(H) where H is the height of the tree
    def dfs(node, current_number):
        if node is None:
            return 0
        current_number = current_number * 10 + node.val
        if node.left is None and node.right is None:
            return current_number
        return dfs(node.left, current_number) + dfs(node.right, current_number)

    return dfs(root, 0)

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(sumNumbers(root))  # Output: 25
