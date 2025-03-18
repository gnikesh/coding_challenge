# You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise). Follow up: Could you do this in-place?


def rotate(matrix):
    """
    Rotates a 2D matrix by 90 degrees clockwise.
    
    Args:
    matrix (list[list[int]]): A 2D matrix.
    
    Returns:
    None
    """
    n = len(matrix)
    
    # Transpose the matrix
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    for i in range(n):
        matrix[i] = matrix[i][::-1]

# Time complexity: O(n^2)
# Space complexity: O(1)
