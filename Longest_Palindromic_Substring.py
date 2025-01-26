# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000. Example: Input: "babad" Output: "bab" Note: "aba" is also a valid answer. Example: Input: "cbbd" Output: "bb"


def longest_palindromic_substring(s: str) -> str:
    def expand_around_center(s: str, left: int, right: int) -> str:
        # Space complexity: O(n) for the string s
        # Time complexity: O(n) for the while loop
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # For every character in the string, consider it as the center of the palindrome
        # Space complexity: O(1)
        # Time complexity: O(n) for the expand_around_center function
        palindrome1 = expand_around_center(s, i, i)
        # For every pair of characters in the string, consider them as the center of the palindrome
        # Space complexity: O(1)
        # Time complexity: O(n) for the expand_around_center function
        palindrome2 = expand_around_center(s, i, i + 1)
        # Choose the longest palindrome
        longest = max([longest, palindrome1, palindrome2], key=len)
    return longest

# Test the function
print(longest_palindromic_substring("babad"))  # Output: "bab"
print(longest_palindromic_substring("cbbd"))  # Output: "bb"
