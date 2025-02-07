# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


def isValid(s: str) -> bool:
    # Time Complexity: O(n), where n is the length of the string
    # Space Complexity: O(n), for the stack in the worst case
    
    stack = []
    hash_table = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in hash_table.values():
            stack.append(char)
        elif char in hash_table:
            if not stack or hash_table[char] != stack.pop():
                return False
    return not stack
