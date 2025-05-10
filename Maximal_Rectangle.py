# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area. For example, given the following matrix: 1 0 1 0 0 1 0 1 1 1 1 1 1 1 1 1 0 0 1 0 Return 6.


def maximalRectangle(matrix):
    # Space complexity: O(n) where n is the number of columns
    # Time complexity: O(m*n) where m and n are the number of rows and columns
    
    if not matrix: return 0
    
    n = len(matrix[0])
    height = [0] * (n + 1)
    res = 0
    
    for row in matrix:
        for i in range(n):
            # Update the height of this point
            height[i] = height[i] + 1 if row[i] == '1' else 0
        
        # Initialize a stack to keep track of the index of the bar
        stack = [-1]
        
        for i in range(n + 1):
            # Keep popping until we find the first bar which is shorter than the current bar
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                # Update the max area
                res = max(res, h * w)
            stack.append(i)
    
    return res
