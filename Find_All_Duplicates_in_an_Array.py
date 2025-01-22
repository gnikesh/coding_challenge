# Given an array of integers, 1 &le; a[i] &le; n (n = size of array), some elements appear twice and others appear once. Find all the elements that appear twice in this array. Could you do it without extra space and in O(n) runtime? Example: Input: [4,3,2,7,8,2,3,1] Output: [2,3]


def find_duplicates(nums):
    duplicates = set()
    for num in nums:
        if nums[abs(num) - 1] < 0:
            duplicates.add(abs(num))
        else:
            nums[abs(num) - 1] *= -1
    return list(duplicates)

# Time complexity: O(n)
# Space complexity: O(n) due to the set
