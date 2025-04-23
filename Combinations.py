# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n. For example, If n = 4 and k = 2, a solution is: [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]


def combine(n, k):
    # Time complexity: O(N choose K) = O(N!/(K!(N-K)!)) 
    # Space complexity: O(N choose K) = O(N!/(K!(N-K)!)), for storing the result
    
    def backtrack(start, path):
        # if the length of the current combination is equal to k, we can add it to the result
        if len(path) == k:
            result.append(path[:])
            return
        # try all numbers from start to n
        for i in range(start, n+1):
            # add the current number to the current combination
            path.append(i)
            # recursively generate all combinations that start with the current combination
            backtrack(i+1, path)
            # remove the last number from the current combination
            path.pop()
            
    result = []
    backtrack(1, [])
    return result

print(combine(4, 2))  # prints: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
