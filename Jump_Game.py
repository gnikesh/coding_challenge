# Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example: A = [2,3,1,1,4], return true. A = [3,2,1,0,4], return false.


def canJump(nums):
    # Initialize a variable to keep track of the last position we can reach
    last_pos = len(nums) - 1
    
    # Iterate over the array from right to left
    for i in range(len(nums) - 1, -1, -1):
        # If the current position can reach the last position we can reach
        if i + nums[i] >= last_pos:
            # Update the last position we can reach
            last_pos = i
    
    # If the last position we can reach is the first position, we can reach the last index
    return last_pos == 0

# Time complexity: O(n)
# Space complexity: O(1)
