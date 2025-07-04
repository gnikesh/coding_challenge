# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum. For example: Given the below binary tree and sum = 22, 5 / \ 4   8 /   / \ 11  13  4 /  \      \ 7    2      1 return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    # Time complexity: O(N) where N is the number of nodes in the tree
    # Space complexity: O(H) where H is the height of the tree
    if not root:
        return False
    
    if not root.left and not root.right:
        return root.val == targetSum
    
    targetSum -= root.val
    
    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)

# Example usage:
# Create the binary tree
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

print(hasPathSum(root, 22))  # Output: True
