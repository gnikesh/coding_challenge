# Follow up for "Search in Rotated Sorted Array": What if duplicates are allowed? Would this affect the run-time complexity? How and why? Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2). Write a function to determine if a given target is in the array. The array may contain duplicates.


def search(nums, target):
    # Time complexity: O(n) in the worst case when the array contains many duplicates
    # Space complexity: O(1) as we are not using any extra space
    if not nums:
        return False

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True

        # if left half is sorted
        if nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # if right half is sorted
        elif nums[left] > nums[mid]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            left += 1

    return False
