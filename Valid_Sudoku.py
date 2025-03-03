# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules. The Sudoku board could be partially filled, where empty cells are filled with the character '.'. A partially filled sudoku which is valid. Note: A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.


def isValidSudoku(board):
    # Initialize sets for each row, column, and box
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Iterate over the board
    for i in range(9):
        for j in range(9):
            # Calculate the box index
            box_index = (i // 3) * 3 + j // 3
            val = board[i][j]
            # Skip empty cells
            if val == '.':
                continue
            # If the value is already in any of the sets, return False
            if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                return False
            # Add the value to the respective sets
            rows[i].add(val)
            cols[j].add(val)
            boxes[box_index].add(val)

    # If no duplicate values are found, return True
    return True

# Time Complexity: O(9*9) = O(1) because the size of the board is constant
# Space Complexity: O(9*9) = O(1) because the size of the board is constant
