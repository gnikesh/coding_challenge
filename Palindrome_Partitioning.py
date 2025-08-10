# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s. For example, given s = "aab", Return [ ["aa","b"], ["a","a","b"] ]


def partition(s):
    def is_palindrome(s):
        # O(n) time complexity
        return s == s[::-1]

    def backtrack(start, path):
        # O(2^n) time complexity
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    result = []
    backtrack(0, [])
    return result

# Example usage
s = "aab"
print(partition(s)) 
# Time complexity: O(2^n * n) 
# Space complexity: O(n) 
