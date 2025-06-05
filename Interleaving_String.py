# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2. For example, Given: s1 = "aabcc", s2 = "dbbca", When s3 = "aadbbcbcac", return true. When s3 = "aadbbbaccc", return false.


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    # Time complexity: O(m*n) where m and n are the lengths of s1 and s2 respectively
    # Space complexity: O(m*n) 
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    dp[0][0] = True

    for i in range(1, len(s1) + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    for j in range(1, len(s2) + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])

    return dp[-1][-1]

# test cases
print(isInterleave("aabcc", "dbbca", "aadbbcbcac"))  # True
print(isInterleave("aabcc", "dbbca", "aadbbbaccc"))  # False
