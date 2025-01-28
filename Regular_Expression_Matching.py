# Implement regular expression matching with support for '.' and '*'. '.' Matches any single character. '*' Matches zero or more of the preceding element. The matching should cover the entire input string (not partial). The function prototype should be: bool isMatch(const char *s, const char *p) Some examples: isMatch("aa","a") → false isMatch("aa","aa") → true isMatch("aaa","aa") → false isMatch("aa", "a*") → true isMatch("aa", ".*") → true isMatch("ab", ".*") → true isMatch("aab", "c*a*b") → true


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Space complexity: O(n * m)
        # Time complexity: O(n * m)
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] in [s[i - 1], '.']:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (p[j - 2] in [s[i - 1], '.']))
        
        return dp[len(s)][len(p)]
