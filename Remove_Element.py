# Given an array and a value, remove all instances of that value in place and return the new length. Do not allocate extra space for another array, you must do this in place with constant memory. The order of elements can be changed. It doesn't matter what you leave beyond the new length. Example: Given input array nums = [3,2,2,3], val = 3 Your function should return length = 2, with the first two elements of nums being 2. Try two pointers. Did you use the property of "the order of elements can be changed"? What happens when the elements to remove are rare?


def removeElement(nums, val):
    """
    Removes all instances of a value from a list in place and returns the new length.

    Args:
    nums (list): The list to remove the value from.
    val (int): The value to remove.

    Returns:
    int: The new length of the list.
    """
    # Initialize two pointers, one at the beginning of the list and one at the beginning of the list.
    i = 0  # This pointer will keep track of the position of the first number that should be kept.
    for j in range(len(nums)):  # This pointer will iterate over the list.
        # If the current number is not equal to the value to be removed, replace the number at the end of the list of kept numbers with the current number.
        if nums[j] != val:
            nums[i] = nums[j]
            # Move the pointer for kept numbers to the right.
            i += 1

    # Return the new length of the list.
    return i

# Time complexity: O(n), where n is the length of the list.
# Space complexity: O(1), since we are not using any additional space that scales with the input size.
