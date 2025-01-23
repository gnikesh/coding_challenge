# Given a string, find the length of the longest substring without repeating characters. Examples: Given "abcabcbb", the answer is "abc", which the length is 3. Given "bbbbb", the answer is "b", with the length of 1. Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Using a sliding window to track the unique characters in the current substring
        left = 0  # Left pointer of the window
        max_length = 0  # Maximum length of substring without repeating characters
        char_index_map = {}  # Map to store the last index of each character in the window
        
        for right, char in enumerate(s):
            # If the character is already in the window, update the left pointer
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1
            
            # Update the last index of the character in the window
            char_index_map[char] = right
            
            # Update the maximum length of substring without repeating characters
            max_length = max(max_length, right - left + 1)
        
        return max_length
# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(k), where k is the number of unique characters in the string
