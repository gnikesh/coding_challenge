# Follow up for "Unique Paths": Now consider if some obstacles are added to the grids. How many unique paths would there be? An obstacle and empty space is marked as 1 and 0 respectively in the grid. For example, There is one obstacle in the middle of a 3x3 grid as illustrated below. [ [0,0,0], [0,1,0], [0,0,0] ] The total number of unique paths is 2. Note: m and n will be at most 100.


def uniquePathsWithObstacles(obstacleGrid):
    # Time complexity: O(m*n) where m and n are dimensions of obstacleGrid
    # Space complexity: O(m*n) for the dp array
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    # Initialize first row and column
    for i in range(m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = 1
        else:
            break
            
    for j in range(n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = 1
        else:
            break
    
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[-1][-1]
