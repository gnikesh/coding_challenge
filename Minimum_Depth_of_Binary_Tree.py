# Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minDepth(root):
    # Time complexity: O(N), where N is the number of nodes in the tree
    # Space complexity: O(N), for the queue in the worst case (when the tree is a linked list)
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    
    while queue:
        node, depth = queue.popleft()
        
        if not node.left and not node.right:
            return depth
        
        if node.left:
            queue.append((node.left, depth + 1))
        
        if node.right:
            queue.append((node.right, depth + 1))
