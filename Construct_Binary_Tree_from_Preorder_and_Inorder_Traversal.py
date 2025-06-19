# Given preorder and inorder traversal of a tree, construct the binary tree. Note: You may assume that duplicates do not exist in the tree.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    # Time complexity: O(n) 
    # Space complexity: O(n)
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])

    return root

def printInorder(root):
    # Time complexity: O(n) 
    # Space complexity: O(h)
    if root:
        printInorder(root.left)
        print(root.val, end=" ")
        printInorder(root.right)

def printPreorder(root):
    # Time complexity: O(n) 
    # Space complexity: O(h)
    if root:
        print(root.val, end=" ")
        printPreorder(root.left)
        printPreorder(root.right)

# Test the function
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = buildTree(preorder, inorder)

print("Preorder traversal of the constructed tree is")
printPreorder(root)
print("\nInorder traversal of the constructed tree is")
printInorder(root)
