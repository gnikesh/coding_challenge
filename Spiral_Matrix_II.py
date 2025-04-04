# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order. For example, Given n = 3, You should return the following matrix: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]


def generateMatrix(n):
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    matrix = [[0]*n for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    dir_index = 0
    row, col = 0, 0
    
    for num in range(1, n*n+1):
        matrix[row][col] = num
        next_row, next_col = row + directions[dir_index][0], col + directions[dir_index][1]
        
        if 0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0:
            row, col = next_row, next_col
        else:
            dir_index = (dir_index + 1) % 4
            row, col = row + directions[dir_index][0], col + directions[dir_index][1]
    
    return matrix
