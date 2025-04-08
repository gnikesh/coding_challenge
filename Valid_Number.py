# Validate if a given string is numeric. Some examples: "0" => true "   0.1  " => true "abc" => false "1 a" => false "2e10" => true Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. Update (2015-02-10): The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.


import re

def isNumber(s: str) -> bool:
    # Remove leading and trailing spaces
    s = s.strip()
    
    # Regular expression pattern for valid numbers
    pattern = re.compile(r'^[-+]?((\d+(\.\d*)?)|(\.\d+))(e[-+]?\d+)?$')
    
    # Check if the string matches the pattern
    return bool(pattern.match(s))

# Time complexity: O(1) - The time complexity of the regex search is technically O(n), 
# where n is the length of the string. However, the problem statement implies that the input string is relatively small.

# Space complexity: O(1) - The space complexity is constant because the regex pattern is constant and doesn't depend on the input size.
