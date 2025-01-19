# Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice. Example: Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].


def two_sum(nums, target):
    num_map = {}  # O(n) space complexity
    for i, num in enumerate(nums):  # O(n) time complexity
        complement = target - num
        if complement in num_map:  # O(1) time complexity
            return [num_map[complement], i]  # O(1) time complexity
        num_map[num] = i  # O(1) time complexity

    return []  # In case no solution is found
