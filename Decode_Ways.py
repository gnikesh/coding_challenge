# A message containing letters from A-Z is being encoded to numbers using the following mapping: 'A' -> 1 'B' -> 2 ... 'Z' -> 26 Given an encoded message containing digits, determine the total number of ways to decode it. For example, Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12). The number of ways decoding "12" is 2.


def numDecodings(s):
    # Time complexity: O(N), where N is the length of string s
    # Space complexity: O(N), where N is the length of string s
    if not s or s[0] == "0":
        return 0
    
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, len(s) + 1):
        # Check if the current character can be decoded
        if s[i-1] != "0":
            dp[i] += dp[i - 1]
        # Check if the current character and the previous one can be decoded together
        if "10" <= s[i-2:i] <= "26":
            dp[i] += dp[i - 2]
    
    return dp[len(s)]
