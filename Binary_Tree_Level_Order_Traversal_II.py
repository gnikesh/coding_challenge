# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root). For example: Given binary tree [3,9,20,null,null,15,7], 3 / \ 9  20 /  \ 15   7 return its bottom-up level order traversal as: [ [15,7], [9,20], [3] ]


from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrderBottom(root):
    # Time complexity: O(N) where N is the number of nodes in the tree
    # Space complexity: O(N) where N is the number of nodes in the tree
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.insert(0, level)
    
    return result

# Example usage:
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# print(levelOrderBottom(root))  # Output: [[15, 7], [9, 20], [3]]
