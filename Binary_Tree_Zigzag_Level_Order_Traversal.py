# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between). For example: Given binary tree [3,9,20,null,null,15,7], 3 / \ 9  20 /  \ 15   7 return its zigzag level order traversal as: [ [3], [20,9], [15,7] ]


from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    # Time complexity: O(N) where N is the number of nodes in the tree
    # Space complexity: O(N) for the queue and result
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level_values = deque()
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if left_to_right:
                level_values.append(node.val)
            else:
                level_values.appendleft(node.val)
                
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(list(level_values))
        left_to_right = not left_to_right
        
    return result
