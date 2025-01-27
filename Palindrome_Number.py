# Determine whether an integer is a palindrome. Do this without extra space. click to show spoilers. Some hints: Could negative integers be palindromes? (ie, -1) If you are thinking of converting the integer to string, note the restriction of using extra space. You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case? There is a more generic way of solving this problem.


def isPalindrome(x: int) -> bool:
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    
    # Negative integers cannot be palindromes
    if x < 0:
        return False

    origin = x
    reversed_num = 0

    while x != 0:
        remainder = x % 10
        reversed_num = reversed_num * 10 + remainder
        x = x // 10

    return origin == reversed_num
