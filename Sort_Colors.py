# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue. Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively. Note: You are not suppose to use the library's sort function for this problem. click to show follow up. Follow up: A rather straight forward solution is a two-pass algorithm using counting sort. First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's. Could you come up with an one-pass algorithm using only constant space?


def sort_colors(nums):
    # Time complexity: O(n)
    # Space complexity: O(1)
    
    # Initialize pointers for 0 and 2
    low, high = 0, len(nums) - 1
    
    # Initialize current pointer
    i = 0
    
    while i <= high:
        if nums[i] == 0:
            # Swap nums[i] and nums[low]
            nums[i], nums[low] = nums[low], nums[i]
            low += 1
            i += 1
        elif nums[i] == 2:
            # Swap nums[i] and nums[high]
            nums[i], nums[high] = nums[high], nums[i]
            high -= 1
        else:
            i += 1

# Test the function
nums = [2, 0, 2, 1, 1, 0]
sort_colors(nums)
print(nums)
