# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one. Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


def singleNumber(nums):
    # Time complexity: O(n), Space complexity: O(1)
    ones = twos = 0
    for num in nums:
        twos |= ones & num
        ones ^= num
        threes = ones & twos
        ones &= ~threes
        twos &= ~threes
    return ones

# Test the function
nums = [2, 2, 3, 2]
print(singleNumber(nums))  # Output: 3
