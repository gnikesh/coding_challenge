# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero. Note: The solution set must not contain duplicate triplets. For example, given array S = [-1, 0, 1, 2, -1, -4], A solution set is: [ [-1, 0, 1], [-1, -1, 2] ]


def three_sum(nums):
    n = len(nums)
    nums.sort()  # Time: O(n log n), Space: O(1)
    triplets = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return triplets

# Test the function
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
