# Implement wildcard pattern matching with support for '?' and '*'. '?' Matches any single character. '*' Matches any sequence of characters (including the empty sequence). The matching should cover the entire input string (not partial). The function prototype should be: bool isMatch(const char *s, const char *p) Some examples: isMatch("aa","a") → false isMatch("aa","aa") → true isMatch("aaa","aa") → false isMatch("aa", "*") → true isMatch("aa", "a*") → true isMatch("ab", "?*") → true isMatch("aab", "c*a*b") → false


def isMatch(s, p):
    # Time complexity: O(len(s) * len(p))
    # Space complexity: O(len(s) * len(p))
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True
    for i in range(1, len(p) + 1):
        if p[i-1] == '*':
            dp[0][i] = dp[0][i-1]
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j-1] in {s[i-1], '?'}:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
    return dp[len(s)][len(p)]

# Example use cases:
print(isMatch("aa", "a"))     # False
print(isMatch("aa", "aa"))    # True
print(isMatch("aaa", "aa"))   # False
print(isMatch("aa", "*"))     # True
print(isMatch("aa", "a*"))    # True
print(isMatch("ab", "?*"))    # True
print(isMatch("aab", "c*a*b")) # False
