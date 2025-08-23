# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words. For example, given s = "leetcode", dict = ["leet", "code"]. Return true because "leetcode" can be segmented as "leet code". UPDATE (2017/1/4): The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


def wordBreak(s: str, wordDict: list[str]) -> bool:
    # Create a set of words for efficient lookup
    word_set = set(wordDict)
    
    # Initialize a list to store whether each substring can be segmented
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    # Iterate over the string
    for i in range(1, len(s) + 1):
        # Check all substrings ending at current position
        for j in range(i):
            # If the substring can be segmented and the remaining part is in the word set
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[-1]

# Time complexity: O(n^2) where n is the length of the string
# Space complexity: O(n) for the dp table, O(m) for the word set where m is the number of words in the dictionary
