# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array. Here are few examples. [1,3,5,6], 5 &#8594; 2 [1,3,5,6], 2 &#8594; 1 [1,3,5,6], 7 &#8594; 4 [1,3,5,6], 0 &#8594; 0


def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Time complexity: O(log n), where n is the length of the input array
# Space complexity: O(1), as no extra space is used that scales with the input size
