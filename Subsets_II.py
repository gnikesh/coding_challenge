# Given a collection of integers that might contain duplicates, nums, return all possible subsets. Note: The solution set must not contain duplicate subsets. For example, If nums = [1,2,2], a solution is: [ [2], [1], [1,2,2], [2,2], [1,2], [] ]


def subsetsWithDup(nums):
    nums.sort()  # sort the list to handle duplicates
    result = []
    def backtrack(start, path):
        # Time complexity: O(2^n) where n is the number of elements in nums
        result.append(path)
        for i in range(start, len(nums)):
            # skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            backtrack(i + 1, path + [nums[i]])
            # Space complexity: O(n * 2^n) for storing all subsets
    backtrack(0, [])
    return result
