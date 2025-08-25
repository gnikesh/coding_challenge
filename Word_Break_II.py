# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words. Return all such possible sentences. For example, given s = "catsanddog", dict = ["cat", "cats", "and", "sand", "dog"]. A solution is ["cats and dog", "cat sand dog"]. UPDATE (2017/1/4): The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


def wordBreak(s, wordDict):
    memo = dict()
    def dfs(s):
        # Time complexity: O(2^n), Space complexity: O(n)
        if s in memo: return memo[s]
        if not s: return []
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                result_of_rest = dfs(s[len(word):])
                for item in result_of_rest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res
    return dfs(s)

# Test
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
print(wordBreak(s, wordDict))
