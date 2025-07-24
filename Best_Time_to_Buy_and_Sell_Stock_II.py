# Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


def maxProfit(prices):
    # Time complexity: O(n) where n is the number of days
    # Space complexity: O(1) as only a constant amount of space is used
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit
