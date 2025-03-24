# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other. Given an integer n, return all distinct solutions to the n-queens puzzle. Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively. For example, There exist two distinct solutions to the 4-queens puzzle: [ [".Q..",  // Solution 1 "...Q", "Q...", "..Q."], ["..Q.",  // Solution 2 "Q...", "...Q", ".Q.."] ]


def solveNQueens(n):
    def is_safe(board, row, col):
        # Check this column on left side
        for i in range(row):
            if board[i][col] == 1:
                return False
    
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
    
        # Check lower diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 1:
                return False
    
        return True

    def solve_n_queens_util(board, row):
        if row == n:
            result = ['.' * i + 'Q' + '.' * (n - i - 1) for i in range(n)]
            results.append(result)
            return
    
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve_n_queens_util(board, row + 1)
                board[row][col] = 0

    results = []
    board = [[0] * n for _ in range(n)]
    solve_n_queens_util(board, 0)
    return results

# Time Complexity: O(n!), where n is the number of queens.
# Space Complexity: O(n), where n is the number of queens.
