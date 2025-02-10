# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. For example, given n = 3, a solution set is: [ "((()))", "(()())", "(())()", "()(())", "()()()" ]


def generate_parentheses(n):
    """
    Generate all combinations of well-formed parentheses.
    """
    def backtrack(open_parentheses, close_parentheses, current_combination):
        # If we have reached the desired length, add the combination to the result.
        if len(current_combination) == 2 * n:
            result.append("".join(current_combination))
            return
        
        # Add an open parenthesis if possible.
        if open_parentheses < n:
            current_combination.append("(")
            backtrack(open_parentheses + 1, close_parentheses, current_combination)
            current_combination.pop()
        
        # Add a close parenthesis if possible.
        if close_parentheses < open_parentheses:
            current_combination.append(")")
            backtrack(open_parentheses, close_parentheses + 1, current_combination)
            current_combination.pop()
    
    result = []
    backtrack(0, 0, [])
    
    return result

# Time complexity: O(4^n / n^(3/2)) due to the nature of catalan numbers
# Space complexity: O(4^n / n^(3/2)) for storing the result and the recursion stack
