# Given a binary tree, determine if it is a valid binary search tree (BST). Assume a BST is defined as follows: The left subtree of a node contains only nodes with keys less than the node's key. The right subtree of a node contains only nodes with keys greater than the node's key. Both the left and right subtrees must also be binary search trees. Example 1: 2 / \ 1   3 Binary tree [2,1,3], return true. Example 2: 1 / \ 2   3 Binary tree [1,2,3], return false.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        # Time complexity: O(N), where N is the number of nodes in the tree (visit each node once)
        # Space complexity: O(H), where H is the height of the tree (for the recursive call stack)
        def validate(node, low=-float('inf'), high=float('inf')):
            if not node:
                return True
            if not low < node.val < high:
                return False
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        return validate(root)

# Test the solution
def main():
    # Create a sample binary tree
    #       2
    #      / \
    #     1   3
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    print(Solution().isValidBST(root1))  # Expected output: True

    # Create another sample binary tree
    #       1
    #      / \
    #     2   3
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print(Solution().isValidBST(root2))  # Expected output: False

if __name__ == "__main__":
    main()
