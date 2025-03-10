# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this in place with constant memory. For example, Given input array nums = [1,1,2], Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.


def removeDuplicates(nums):
    # Time complexity: O(n), where n is the number of elements in the input array.
    # Space complexity: O(1), constant space complexity as required.
    
    if not nums:
        return 0
    
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1

# Test the function
nums = [1,1,2]
new_length = removeDuplicates(nums)
print("New length:", new_length)
