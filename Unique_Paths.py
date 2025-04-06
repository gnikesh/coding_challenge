# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below). The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below). How many possible unique paths are there? Above is a 3 x 7 grid. How many possible unique paths are there? Note: m and n will be at most 100.


def uniquePaths(m, n):
    # Create a 2D array to store the number of unique paths to each cell
    dp = [[1]*n for _ in range(m)]
    
    # Fill up the dp array
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # The number of unique paths to the bottom-right corner is stored in the last cell of the dp array
    return dp[-1][-1]

# Time complexity: O(m*n) where m and n are the dimensions of the grid
# Space complexity: O(m*n) where m and n are the dimensions of the grid
