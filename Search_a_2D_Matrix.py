# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties: Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row. For example, Consider the following matrix: [ [1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50] ] Given target = 3, return true.


def searchMatrix(matrix, target):
    # Time complexity: O(m + n), where m and n are the number of rows and columns in the matrix
    # Space complexity: O(1), excluding the input space

    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1

    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1

    return False

# Example usage:
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 3
print(searchMatrix(matrix, target))  # Output: True
