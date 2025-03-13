# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2. Note: The length of both num1 and num2 is < 110. Both num1 and num2 contains only digits 0-9. Both num1 and num2 does not contain any leading zero. You must not use any built-in BigInteger library or convert the inputs to integer directly.


def multiply(num1: str, num2: str) -> str:
    # Convert input strings to lists of integers for easier manipulation
    num1, num2 = list(map(int, num1)), list(map(int, num2))
    
    # Reverse the lists to perform multiplication from right to left
    num1, num2 = num1[::-1], num2[::-1]
    
    # Initialize a list to store the result
    result = [0] * (len(num1) + len(num2))
    
    # Perform multiplication and store the result
    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i + j] += num1[i] * num2[j]
            
    # Propagate carry-over values
    for i in range(len(result) - 1):
        if result[i] >= 10:
            result[i + 1] += result[i] // 10
            result[i] %= 10
            
    # Remove leading zeros
    result = result[::-1]
    start = 0
    while start < len(result) and result[start] == 0:
        start += 1
        
    # Convert the result back to a string
    return ''.join(map(str, result[start:])) if start < len(result) else '0'

# Time complexity: O(n*m) where n and m are the lengths of num1 and num2
# Space complexity: O(n + m) where n and m are the lengths of num1 and num2
