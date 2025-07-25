# Say you have an array for which the ith element is the price of a given stock on day i. If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit. Example 1: Input: [7, 1, 5, 3, 6, 4] Output: 5 max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price) Example 2: Input: [7, 6, 4, 3, 1] Output: 0 In this case, no transaction is done, i.e. max profit = 0.


def maxProfit(prices):
    # Time complexity: O(n), where n is the number of days
    # Space complexity: O(1), as we are using a constant amount of space
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit

# Example usage:
print(maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(maxProfit([7, 6, 4, 3, 1]))  # Output: 0
