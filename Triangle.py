# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below. For example, given the following triangle [ [2], [3,4], [6,5,7], [4,1,8,3] ] The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11). Note: Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


def minimumTotal(triangle):
    # Time complexity: O(n*m) where n is the number of rows and m is the maximum number of columns
    # Space complexity: O(n) where n is the number of rows 
    if not triangle:
        return 0
    n = len(triangle)
    # Create a copy of the last row in the triangle
    dp = triangle[-1]
    for i in range(n-2, -1, -1):
        for j in range(len(triangle[i])):
            # Update each element to be the minimum sum it can get to the bottom
            dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
    # The minimum path sum from top to bottom is stored in the first element of dp
    return dp[0]

def main():
    triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
    print(minimumTotal(triangle))

main()
