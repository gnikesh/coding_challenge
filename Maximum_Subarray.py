# Find the contiguous subarray within an array (containing at least one number) which has the largest sum. For example, given the array [-2,1,-3,4,-1,2,1,-5,4], the contiguous subarray [4,-1,2,1] has the largest sum = 6. click to show more practice. More practice: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


def max_subarray(nums):
    """
    This function finds the maximum sum of a subarray within the given array.
    
    Parameters:
    nums (list): A list of integers.
    
    Returns:
    int: The maximum sum of a subarray.
    """
    if not nums:
        return 0
    
    # Initialize the maximum sum and current sum to the first element of the array
    max_sum = current_sum = nums[0]
    
    # Iterate over the array starting from the second element
    for num in nums[1:]:
        # Update the current sum to be the maximum of the current number and the sum of the current number and previous current sum
        current_sum = max(num, current_sum + num)
        
        # Update the maximum sum to be the maximum of the current maximum sum and the current sum
        max_sum = max(max_sum, current_sum)
    
    # Return the maximum sum
    return max_sum

# Time complexity: O(n), where n is the number of elements in the array.
# Space complexity: O(1), as we are using a constant amount of space.
