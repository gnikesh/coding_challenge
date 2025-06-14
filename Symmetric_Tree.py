# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center). For example, this binary tree [1,2,2,3,4,4,3] is symmetric: 1 / \ 2   2 / \ / \ 3  4 4  3 But the following [1,2,2,null,3,null,3]  is not: 1 / \ 2   2 \   \ 3    3 Note: Bonus points if you could solve it both recursively and iteratively.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive solution
def isSymmetricRecursive(root):
    # Time complexity: O(n) where n is the number of nodes in the tree
    # Space complexity: O(h) where h is the height of the tree
    def isMirror(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

    return isMirror(root, root)

# Iterative solution
def isSymmetricIterative(root):
    # Time complexity: O(n) where n is the number of nodes in the tree
    # Space complexity: O(n/2) in the worst case, O(log n) in the best case (when the tree is balanced)
    if root is None:
        return True

    queue = [(root.left, root.right)]
    while queue:
        t1, t2 = queue.pop(0)
        if t1 is None and t2 is None:
            continue
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False
        queue.append((t1.left, t2.right))
        queue.append((t1.right, t2.left))

    return True

# Test the functions
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
print(isSymmetricRecursive(root))  # Output: True
print(isSymmetricIterative(root))  # Output: True
