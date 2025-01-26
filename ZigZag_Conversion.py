# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) P   A   H   N A P L S I I G Y   I   R And then read line by line: "PAHNAPLSIIGYIR" Write the code that will take a string and make this conversion given a number of rows: string convert(string text, int nRows); convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


def convert(s, numRows):
    # Time complexity: O(n) where n is the length of string s
    # Space complexity: O(n) for storing characters in each row
    if numRows == 1 or numRows >= len(s):
        return s
    
    rows = [''] * numRows
    index, step = 0, 1
    
    for char in s:
        rows[index] += char
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step
    
    # Time complexity: O(n) for concatenating strings
    # Space complexity: O(n) for storing the final result
    return ''.join(rows)

# Test the function
print(convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
