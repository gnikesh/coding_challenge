# Given an unsorted array of integers, find the length of the longest consecutive elements sequence. For example, Given [100, 4, 200, 1, 3, 2], The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4. Your algorithm should run in O(n) complexity.


def longest_consecutive_sequence(nums):
    # Create a set from the list for O(1) lookups 
    num_set = set(nums)
    
    longest_sequence = 0
    
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
            
            # Check numbers that are consecutive to current_num
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
            
            # Update the longest sequence if necessary
            longest_sequence = max(longest_sequence, current_sequence)
    
    return longest_sequence

# Time complexity: O(n) 
# Space complexity: O(n)
