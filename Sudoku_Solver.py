# Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by the character '.'. You may assume that there will be only one unique solution. A sudoku puzzle... ...and its solution numbers marked in red.


def solveSudoku(board):
    # Time complexity: O(9^81), Space complexity: O(1)
    
    def is_valid(board, row, col, num):
        # Check the number in the row
        for x in range(9):
            if board[row][x] == str(num):
                return False
                
        # Check the number in the column
        for x in range(9):
            if board[x][col] == str(num):
                return False

        # Check the number in the box
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == str(num):
                    return False
        return True

    def solve(board):
        # Time complexity: O(9^81), Space complexity: O(1)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = str(num)
                            if solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    solve(board)

    # Convert 2D list to string list for desired output format
    for i in range(len(board)):
        board[i] = "".join(board[i])

# Test the function
board = [
         ["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]
        ]

solveSudoku(board)
for row in board:
    print(row)
