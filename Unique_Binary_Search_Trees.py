# Given n, how many structurally unique BST's (binary search trees) that store values 1...n? For example, Given n = 3, there are a total of 5 unique BST's. 1         3     3      2      1 \       /     /      / \      \ 3     2     1      1   3      2 /     /       \                 \ 2     1         2                 3


def numTrees(n: int) -> int:
    # Create a list to store the number of unique BSTs for each n
    # Time complexity: O(n), Space complexity: O(n)
    dp = [0] * (n + 1)
    
    # Base case: There is only one way to construct an empty tree
    # Time complexity: O(1), Space complexity: O(1)
    dp[0] = 1
    dp[1] = 1
    
    # For each number of nodes
    # Time complexity: O(n^2), Space complexity: O(n)
    for i in range(2, n + 1):
        # For each possible root node
        for j in range(i):
            # The number of unique BSTs is the product of the number of unique left and right subtrees
            dp[i] += dp[j] * dp[i - j - 1]
    
    # Return the number of unique BSTs for the given n
    # Time complexity: O(1), Space complexity: O(1)
    return dp[n]

# Total time complexity: O(n^2), Total space complexity: O(n)
