# Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once. Example 1: Input: [1,1,2,3,3,4,4,8,8] Output: 2 Example 2: Input: [3,3,7,7,10,11,11] Output: 10 Note: Your solution should run in O(log n) time and O(1) space.


def singleElement(nums):
    """
    Function to find a single element in a sorted array where every other element appears twice.

    Time complexity: O(log n)
    Space complexity: O(1)
    
    :param nums: A sorted list of integers with all except one element repeated twice.
    :return: The unique element that appears only once.
    """
    # Initialize two pointers, low and high, to start from both ends
    low, high = 0, len(nums) - 1
    
    while low < high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # Count the number of times the middle element is repeated
        count = sum(1 for i in range(mid + 1) if nums[i] == nums[mid])
        
        # If the middle element appears once, it's our answer
        if count < mid + 1:
            return nums[mid]
        
        # If the left half has more than half of the sum of all numbers,
        # move the high pointer to the middle index
        elif (count - (len(nums) - i)) > i for i in range(mid + 2, len(nums))):
            low = mid + 1
        
        # Move the high pointer to the left
        else:
            high = mid

# Test cases
print(singleElement([1,1,2,3,3,4,4,8,8]))  # Output: 2
print(singleElement([3,3,7,7,10,11,11]))  # Output: 10
