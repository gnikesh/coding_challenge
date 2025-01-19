# You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin. Note: You can assume that 0 <= amount <= 5000 1 <= coin <= 5000 the number of coins is less than 500 the answer is guaranteed to fit into signed 32-bit integer Example 1: Input: amount = 5, coins = [1, 2, 5] Output: 4 Explanation: there are four ways to make up the amount: 5=5 5=2+2+1 5=2+1+1+1 5=1+1+1+1+1 Example 2: Input: amount = 3, coins = [2] Output: 0 Explanation: the amount of 3 cannot be made up just with coins of 2. Example 3: Input: amount = 10, coins = [10] Output: 1


def change(amount: int, coins: list) -> int:
    # Create a list to store the number of combinations for each amount from 0 to target
    dp = [0] * (amount + 1)
    
    # There is one way to make up the amount of 0 (i.e., not using any coins)
    dp[0] = 1
    
    # For each coin
    for coin in coins:
        # For each amount from the coin value to the target
        for i in range(coin, amount + 1):
            # The number of combinations for the current amount is the sum of the number of combinations for the amount without the current coin and the number of combinations for the amount minus the current coin
            dp[i] += dp[i - coin]
    
    # Return the number of combinations for the target amount
    return dp[amount]

# Time complexity: O(amount * len(coins))
# Space complexity: O(amount)
