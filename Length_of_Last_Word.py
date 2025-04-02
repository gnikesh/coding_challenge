# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string. If the last word does not exist, return 0. Note: A word is defined as a character sequence consists of non-space characters only. For example, Given s = "Hello World", return 5.


def lengthOfLastWord(s: str) -> int:
    # split the string into words
    words = s.split()
    
    # if the list of words is empty, return 0
    if not words:
        return 0
    
    # return the length of the last word
    return len(words[-1])

# Time complexity: O(n), where n is the length of the string.
# Space complexity: O(n), where n is the number of words in the string.
