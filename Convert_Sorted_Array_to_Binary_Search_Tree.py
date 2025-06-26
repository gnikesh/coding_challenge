# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    # Base case
    if not nums:
        return None
    
    # Find the middle index
    mid = len(nums) // 2
    
    # Create a new node with the middle element
    node = TreeNode(nums[mid])
    
    # Recursively create the left and right subtrees
    node.left = sorted_array_to_bst(nums[:mid])
    node.right = sorted_array_to_bst(nums[mid+1:])
    
    return node

# Time complexity: O(N) where N is the number of elements in the array 
# Space complexity: O(log N) due to the recursive call stack
