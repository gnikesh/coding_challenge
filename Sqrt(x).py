# Implement int sqrt(int x). Compute and return the square root of x.


class Solution:
    def mySqrt(self, x: int) -> int:
        # Time complexity: O(log n)
        # Space complexity: O(1)
        
        if x < 2:
            return x
        
        left, right = 1, x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            
            if num == x:
                return mid
            elif num < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return left - 1
