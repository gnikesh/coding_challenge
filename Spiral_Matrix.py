# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order. For example, Given the following matrix: [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ] You should return [1,2,3,6,9,8,7,4,5].


def spiralOrder(matrix):
    # Time complexity: O(m * n) where m and n are the number of rows and columns in the matrix
    # Space complexity: O(m * n) for the result list
    if not matrix:
        return []
    
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Check if the bounds are within the matrix
        if top <= bottom and left <= right:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

# Test the function
print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
