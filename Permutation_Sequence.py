# The set [1,2,3,&#8230;,n] contains a total of n! unique permutations. By listing and labeling all of the permutations in order, We get the following sequence (ie, for n = 3): "123" "132" "213" "231" "312" "321" Given n and k, return the kth permutation sequence. Note: Given n will be between 1 and 9 inclusive.


import math

def getPermutation(n, k):
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    
    # Generate a list of numbers from 1 to n
    factorial = math.factorial
    numbers = list(range(1, n + 1))
    permutation = ''
    
    # Subtract 1 because we're working with 0-based indexing
    k -= 1
    
    # Calculate the factorial of n and then keep dividing k by the factorial of remaining numbers
    for i in range(1, n + 1):
        idx = k // factorial(n - i)
        permutation += str(numbers[idx])
        # Remove the number that we've used from the list
        numbers.pop(idx)
        # If there are remaining numbers, update k
        if i < n:
            k %= factorial(n - i)
    
    return permutation
