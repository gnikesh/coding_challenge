# Given a string s, partition s such that every substring of the partition is a palindrome. Return the minimum cuts needed for a palindrome partitioning of s. For example, given s = "aab", Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


def minCut(s: str) -> int:
    n = len(s)
    # is_palindrome[i][j] will be 'true' if the string from index i to j is palindrome.
    is_palindrome = [[False] * n for _ in range(n)]
    
    # All substrings with one character are palindromes
    for i in range(n):
        is_palindrome[i][i] = True

    # Check for substring of length 2.
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_palindrome[i][i + 1] = True

    # Check for lengths greater than 2.
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                is_palindrome[i][j] = True

    # dp[i] will be the minimum cuts needed for a palindrome partitioning of s[0:i]
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        if is_palindrome[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if is_palindrome[j + 1][i] and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1

    # Time complexity: O(n^2) 
    # Space complexity: O(n^2)
    return dp[-1]

# Example usage
print(minCut("aab"))  # Output: 1
