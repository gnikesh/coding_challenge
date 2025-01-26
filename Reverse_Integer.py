# Reverse digits of an integer. Example1: x =  123, return  321 Example2: x = -123, return -321 click to show spoilers. Have you thought about this? Here are some good questions to ask before coding. Bonus points for you if you have already thought through this! If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100. Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases? For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows. Note: The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.


def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    x *= sign
    
    reversed_num = 0
    while x:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
        
        # Space complexity: O(1)
        # Time complexity: O(log|x|)
    
    # Check for overflow
    if reversed_num > 2**31 - 1:
        return 0
    
    return sign * reversed_num
