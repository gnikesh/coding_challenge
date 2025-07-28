# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases. For example, "A man, a plan, a canal: Panama" is a palindrome. "race a car" is not a palindrome. Note: Have you consider that the string might be empty? This is a good question to ask during an interview. For the purpose of this problem, we define empty string as valid palindrome.


def is_palindrome(s: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    # Initialize two pointers, one at the start and one at the end of the string
    left, right = 0, len(s) - 1
    
    # Compare characters from the start and end, moving towards the center
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    # If all pairs of characters match, the string is a palindrome
    return True

# Time complexity: O(n), where n is the length of the string
# Space complexity: O(n), where n is the length of the string
