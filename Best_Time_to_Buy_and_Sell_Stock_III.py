# Say you have an array for which the ith element is the price of a given stock on day i. Design an algorithm to find the maximum profit. You may complete at most two transactions. Note: You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


def maxProfit(prices):
    # Time complexity: O(n)
    # Space complexity: O(1)
    buy1, sell1, buy2, sell2 = float('-inf'), 0, float('-inf'), 0
    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)
    return sell2

# Test the function
print(maxProfit([3,3,5,0,0,3,1,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))
