# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers. If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order). The replacement must be in-place, do not allocate extra memory. Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column. 1,2,3 &#8594; 1,3,2 3,2,1 &#8594; 1,2,3 1,1,5 &#8594; 1,5,1


def nextPermutation(nums):
    # Find the largest index k such that nums[k] < nums[k + 1]
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            break

    # If we didn't find such a pair of two successive numbers in increasing order
    else:
        nums.reverse()
        return

    # Find the largest index l > k such that nums[k] < nums[l]
    for j in range(len(nums) - 1, i, -1):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            break

    # Reverse the sequence after index k
    nums[i + 1:] = reversed(nums[i + 1:])

# Time complexity: O(n) where n is the length of nums
# Space complexity: O(1) as it only uses a constant amount of space
