# Follow up for "Remove Duplicates": What if duplicates are allowed at most twice? For example, Given sorted array nums = [1,1,1,2,2,3], Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.


def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    
    i = 0  # Time complexity of outer loop is O(n)
    for n in nums:  # Time complexity of this loop is O(n)
        if i < 2 or n > nums[i-2]:  # Check for duplicate at most twice
            nums[i] = n
            i += 1
    
    return i  # Return the length of the new array

# Time complexity: O(n)
# Space complexity: O(1)
