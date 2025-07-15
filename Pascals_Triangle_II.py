# Given an index k, return the kth row of the Pascal's triangle. For example, given k = 3, Return [1,3,3,1]. Note: Could you optimize your algorithm to use only O(k) extra space?


def getRow(k: int) -> list[int]:
    row = [1]
    # Time complexity: O(k^2) 
    # Space complexity: O(k)
    for _ in range(k):
        row = [x + y for x, y in zip([0] + row, row + [0])]
    return row

# Example usage:
print(getRow(3))  # Output: [1, 3, 3, 1]
