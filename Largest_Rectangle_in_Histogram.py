# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram. Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3]. The largest rectangle is shown in the shaded area, which has area = 10 unit. For example, Given heights = [2,1,5,6,2,3], return 10.


def largestRectangleArea(heights):
    stack = []
    max_area = 0
    index = 0
    
    while index < len(heights):
        # If the stack is empty or the current height is greater than or equal to the height at the top of the stack, push the current index to the stack
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # If the current height is less than the height at the top of the stack, calculate the area of the rectangle with the height at the top of the stack as the smallest bar
            top_of_stack = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, heights[top_of_stack] * width)
    
    # Calculate the area of the rectangles with the remaining heights in the stack
    while stack:
        top_of_stack = stack.pop()
        width = index if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, heights[top_of_stack] * width)
    
    return max_area

# Time complexity: O(n) where n is the number of bars in the histogram
# Space complexity: O(n) where n is the number of bars in the histogram
