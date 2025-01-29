# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water. Note: You may not slant the container and n is at least 2.


def maxArea(height):
    # Initialize two pointers at the start and end of the list
    left, right = 0, len(height) - 1
    
    # Initialize the maximum area
    max_area = 0
    
    # Traverse the list from both sides
    while left < right:
        # Calculate the area of the current container
        area = (right - left) * min(height[left], height[right])
        
        # Update the maximum area if the current area is larger
        max_area = max(max_area, area)
        
        # Move the pointer of the shorter line towards the center
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Time complexity: O(n), where n is the number of lines
# Space complexity: O(1), as it only uses a constant amount of space
