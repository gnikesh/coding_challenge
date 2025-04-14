# You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? Note: Given n will be a positive integer.


def climbStairs(n: int) -> int:
    # Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2

    # Initialize dp array with base cases
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    # Fill up dp array
    for i in range(3, n + 1):
        # Time complexity: O(n)
        dp[i] = dp[i - 1] + dp[i - 2]

    # Return result
    return dp[n]

# Time complexity: O(n)
# Space complexity: O(n)
