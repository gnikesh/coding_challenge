# Given a set of distinct integers, nums, return all possible subsets. Note: The solution set must not contain duplicate subsets. For example, If nums = [1,2,3], a solution is: [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ]


def subsets(nums):
    # Time complexity: O(N * 2^N), where N is the number of elements in the input set
    # Space complexity: O(N * 2^N), for storing all subsets
    
    n = len(nums)
    output = []
    
    for i in range(2**n, 2**(n+1)):
        # Generate binary string for subset
        binary = bin(i)[3:]
        
        subset = []
        for j in range(n):
            if binary[j] == '1':
                subset.append(nums[j])
        
        # Add subset to output list
        output.append(subset)
    
    return output

# Test the function
nums = [1, 2, 3]
print(subsets(nums))
