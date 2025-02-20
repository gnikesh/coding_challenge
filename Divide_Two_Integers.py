# Divide two integers without using multiplication, division and mod operator. If it is overflow, return MAX_INT.


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                i <<= 1
            dividend -= temp
            quotient += i

        quotient *= sign

        return max(min(quotient, MAX_INT), MIN_INT)


# Time Complexity: O(log(N))  - where N is the dividend
# Space Complexity: O(1)      - no extra space used, only a constant amount of space
