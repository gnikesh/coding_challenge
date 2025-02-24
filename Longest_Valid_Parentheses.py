# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring. For "(()", the longest valid parentheses substring is "()", which has length = 2. Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.


def longestValidParentheses(s):
    stack = [-1]  # Initialize with -1 to handle edge cases
    max_len = 0
    
    # Traverse the string
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:  # If stack is empty, push the current index
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])  # Update max length
    
    return max_len

# Time complexity: O(n), n is the length of the string
# Space complexity: O(n), in the worst case, the stack will store n elements
