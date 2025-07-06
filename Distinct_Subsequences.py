# Given a string S and a string T, count the number of distinct subsequences of T in S. A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not). Here is an example: S = "rabbbit", T = "rabbit" Return 3.


def numDistinct(S, T):
    m, n = len(T), len(S)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    # base case: there is one way to get an empty subsequence
    for i in range(n+1):
        dp[0][i] = 1
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            # if current characters match, consider two cases: 
            #   include current character or exclude it
            if T[i-1] == S[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            else:
                # if current characters don't match, exclude current character
                dp[i][j] = dp[i][j-1]
    
    # Time complexity: O(m*n) 
    # Space complexity: O(m*n)
    return dp[m][n]

# example usage:
S = "rabbbit"
T = "rabbit"
print(numDistinct(S, T))  # output: 3
