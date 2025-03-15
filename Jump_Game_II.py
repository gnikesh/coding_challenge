# Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. For example: Given array A = [2,3,1,1,4] The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.) Note: You can assume that you can always reach the last index.


def jump(nums):
    # Time complexity: O(n), where n is the number of elements in the array
    # Space complexity: O(1), as we only use a constant amount of space

    if len(nums) < 2:
        return 0

    max_reach = nums[0]
    step = nums[0]
    jumps = 1

    for i in range(1, len(nums)):
        if i == len(nums) - 1:
            return jumps

        max_reach = max(max_reach, i + nums[i])
        step -= 1

        if step == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            step = max_reach - i

# Example usage:
print(jump([2,3,1,1,4]))  # Output: 2
