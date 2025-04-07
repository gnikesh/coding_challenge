# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. Note: You can only move either down or right at any point in time.


def minPathSum(grid):
    # Time complexity: O(m * n), where m and n are the dimensions of the grid
    # Space complexity: O(m * n)
    
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    
    # Initialize first row and column with cumulative sums
    for i in range(1, rows):
        grid[i][0] += grid[i - 1][0]
        
    for j in range(1, cols):
        grid[0][j] += grid[0][j - 1]
        
    # Fill the rest of the grid
    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
            
    return grid[-1][-1]
