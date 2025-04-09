# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer. You may assume the integer do not contain any leading zero, except the number 0 itself. The digits are stored such that the most significant digit is at the head of the list.


def plusOne(digits):
    # Time complexity: O(n), where n is the number of digits
    # Space complexity: O(1), since the space needed does not grow with input size, 
    # it's just the space for the carry variable and the function call stack

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    
    # If all digits were 9, return [1] + digits to account for the extra digit
    return [1] + digits
