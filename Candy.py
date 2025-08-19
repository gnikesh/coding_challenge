# There are N children standing in a line. Each child is assigned a rating value. You are giving candies to these children subjected to the following requirements: Each child must have at least one candy. Children with a higher rating get more candies than their neighbors. What is the minimum candies you must give?


def candy(ratings):
    n = len(ratings)
    candies = [1] * n  # Initialize each child with 1 candy
    # Pass 1: From left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            # If current child's rating is higher than the previous, give one more candy
            candies[i] = candies[i - 1] + 1 
    # Pass 2: From right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
            # If current child's rating is higher than the next and has less or equal candies, update
            candies[i] = candies[i + 1] + 1 
    # Return the total number of candies
    return sum(candies) 
# Time complexity: O(n)
# Space complexity: O(n)
