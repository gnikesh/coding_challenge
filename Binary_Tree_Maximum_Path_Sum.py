# Given a binary tree, find the maximum path sum. For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root. For example: Given the below binary tree, 1 / \ 2   3 Return 6.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        # Time complexity: O(N), where N is the number of nodes in the tree
        # Space complexity: O(H), where H is the height of the tree
        self.dfs(root)
        return self.max_sum

    def dfs(self, node: TreeNode) -> int:
        # Base case
        if not node:
            return 0

        # Recursively calculate the maximum path sum of the left and right subtrees
        left_sum = max(self.dfs(node.left), 0)
        right_sum = max(self.dfs(node.right), 0)

        # Update the maximum path sum if the current path sum is greater
        self.max_sum = max(self.max_sum, node.val + left_sum + right_sum)

        # Return the maximum path sum of the current node and its subtrees
        return node.val + max(left_sum, right_sum)


# Example usage:
# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Find the maximum path sum
solution = Solution()
max_sum = solution.maxPathSum(root)
print(max_sum)  # Output: 6
