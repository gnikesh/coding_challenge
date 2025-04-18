# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place. click to show follow up. Follow up: Did you use extra space? A straight forward solution using O(mn) space is probably a bad idea. A simple improvement uses O(m + n) space, but still not the best solution. Could you devise a constant space solution?


def setZeroes(matrix):
    # Get the number of rows and columns
    rows, cols = len(matrix), len(matrix[0])

    # Use first row and first column to track zeros
    first_row_zero = False
    first_col_zero = False

    # Initialize flags for first row and column
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True

    # Mark zeros in rows and columns
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Nullify rows and columns based on marks
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Nullify first row and column if necessary
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0
    
    # Time complexity: O(m*n), Space complexity: O(1)
