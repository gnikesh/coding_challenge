# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value. Your algorithm's runtime complexity must be in the order of O(log n). If the target is not found in the array, return [-1, -1]. For example, Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].


def searchRange(nums, target):
    def binary_search(nums, target, find_first):
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    return [binary_search(nums, target, True), binary_search(nums, target, False)]
# Time complexity: O(log n) 
# Space complexity: O(1)
