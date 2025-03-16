# Given a collection of distinct numbers, return all possible permutations. For example, [1,2,3] have the following permutations: [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]


def permute(nums):
    """
    Given a collection of distinct numbers, return all possible permutations.
    
    Args:
        nums (list): A list of distinct numbers.
    
    Returns:
        list: A list of lists, where each sublist is a permutation of the input list.
    """
    def backtrack(first = 0):
        # if all integers are used up
        if first == n:  
            output.append(nums[:])
        for i in range(first, n):
            # place i-th integer first 
            # in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]
            
    n = len(nums)
    output = []
    backtrack()
    return output

# Example usage:
print(permute([1,2,3]))

# Time complexity: O(n*n!), where n is the length of the input list. 
# This is because there are n! permutations and generating each permutation takes O(n) time.

# Space complexity: O(n*n!), where n is the length of the input list. 
# This is because we need to store all n! permutations, and each permutation takes O(n) space.
