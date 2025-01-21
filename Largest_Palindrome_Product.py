# Find the largest palindrome made from the product of two n-digit numbers. Since the result could be very large, you should return the largest palindrome mod 1337. Example: Input: 2 Output: 987 Explanation: 99 x 91 = 9009, 9009 % 1337 = 987 Note: The range of n is [1,8].


def largest_palindrome(n):
    # Time complexity: O(n^2), Space complexity: O(1)
    max_num = 10**n - 1
    min_num = 10**(n-1)
    
    max_palindrome = 0
    
    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):
            product = i * j
            if str(product) == str(product)[::-1] and product > max_palindrome:
                max_palindrome = product
                
    return max_palindrome % 1337

# Test the function
print(largest_palindrome(2))
