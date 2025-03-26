# Follow up for N-Queens problem. Now, instead outputting board configurations, return the total number of distinct solutions.


def totalNQueens(n: int) -> int:
    # Time complexity: O(n!) 
    # Space complexity: O(n)
    def isSafe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
                return False
        return True

    def solveNQueens(board, row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if isSafe(board, row, col):
                board[row] = col
                count += solveNQueens(board, row + 1)
        return count

    board = [-1] * n
    return solveNQueens(board, 0)
