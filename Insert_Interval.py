# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary). You may assume that the intervals were initially sorted according to their start times. Example 1: Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9]. Example 2: Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16]. This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].


def insert_interval(intervals, new_interval):
    # Time complexity: O(n) where n is the number of intervals
    # Space complexity: O(n) for the output
    
    start, end = new_interval
    left, right = [], []
    
    for i in intervals:
        if i[1] < start:
            left += [i]
        elif i[0] > end:
            right += [i]
        else:
            start = min(i[0], start)
            end = max(i[1], end)
            
    return left + [[start, end]] + right


# Test the function
print(insert_interval([[1,3],[6,9]], [2,5]))  # Output: [[1,5],[6,9]]
print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9]))  # Output: [[1,2],[3,10],[12,16]]
