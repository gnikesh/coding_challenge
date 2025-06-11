# Given two binary trees, write a function to check if they are equal or not. Two binary trees are considered equal if they are structurally identical and the nodes have the same value.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(p, q):
    # Time complexity: O(N), where N is the total number of nodes in the trees
    # Space complexity: O(H), where H is the height of the trees
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def isSameTree_iterative(p, q):
    # Time complexity: O(N), where N is the total number of nodes in the trees
    # Space complexity: O(N), where N is the total number of nodes in the trees
    stack = [(p, q)]
    while stack:
        node_p, node_q = stack.pop()
        if not node_p and not node_q:
            continue
        if not node_p or not node_q:
            return False
        if node_p.val != node_q.val:
            return False
        stack.append((node_p.left, node_q.left))
        stack.append((node_p.right, node_q.right))
    return True
