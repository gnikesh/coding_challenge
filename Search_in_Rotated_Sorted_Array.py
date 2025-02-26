# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2). You are given a target value to search. If found in the array return its index, otherwise return -1. You may assume no duplicate exists in the array.


def search(nums, target):
    # Time complexity: O(log n), where n is the number of elements in the array
    # Space complexity: O(1), no extra space used
    
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        
        # If target found, return its index
        if nums[mid] == target:
            return mid
        
        # If left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                # If target is in the left half, update right pointer
                right = mid - 1
            else:
                # If target is not in the left half, update left pointer
                left = mid + 1
        # If right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                # If target is in the right half, update left pointer
                left = mid + 1
            else:
                # If target is not in the right half, update right pointer
                right = mid - 1
                
    # If target not found, return -1
    return -1
