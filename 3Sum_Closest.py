# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution. For example, given array S = {-1 2 1 -4}, and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


def threeSumClosest(nums, target):
    nums.sort()
    res = float('inf')
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if abs(s - target) < abs(res - target):
                res = s
            if s < target:
                left += 1
            else:
                right -= 1
    return res

# Time complexity: O(n^2)
# Space complexity: O(1)
