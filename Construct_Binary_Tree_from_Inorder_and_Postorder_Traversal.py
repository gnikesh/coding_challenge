# Given inorder and postorder traversal of a tree, construct the binary tree. Note: You may assume that duplicates do not exist in the tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        # Time complexity: O(n), Space complexity: O(n)
        if not inorder or not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        
        return root

def printInorder(root):
    # Time complexity: O(n), Space complexity: O(n)
    if root is not None:
        printInorder(root.left)
        print(root.val, end=" ")
        printInorder(root.right)

def printPostorder(root):
    # Time complexity: O(n), Space complexity: O(n)
    if root is not None:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val, end=" ")

# Example usage
inorder = [4, 2, 5, 1, 3, 6]
postorder = [4, 5, 2, 6, 3, 1]

solution = Solution()
root = solution.buildTree(inorder, postorder)

print("Inorder Traversal: ")
printInorder(root)  # Output: 4 2 5 1 3 6
print("\nPostorder Traversal: ")
printPostorder(root)  # Output: 4 5 2 6 3 1
