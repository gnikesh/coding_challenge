# Given a collection of intervals, merge all overlapping intervals. For example, Given [1,3],[2,6],[8,10],[15,18], return [1,6],[8,10],[15,18].


def merge_intervals(intervals):
    # Time complexity: O(n log n)
    # Space complexity: O(n)
    if not intervals:
        return []
    
    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    
    merged_intervals = [intervals[0]]
    for current_interval in intervals[1:]:
        last_merged_interval = merged_intervals[-1]
        
        # If current interval overlaps the last merged interval, merge them
        if current_interval[0] <= last_merged_interval[1]:
            # Update the end time of the last merged interval
            merged_intervals[-1] = [last_merged_interval[0], max(last_merged_interval[1], current_interval[1])]
        else:
            # Add the current interval to the list of merged intervals
            merged_intervals.append(current_interval)
    
    return merged_intervals

# Example usage:
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))  # Output: [[1,6],[8,10],[15,18]]
