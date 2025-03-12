# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining. For example, Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6. The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!


def trap(height):
    # Time complexity: O(n)
    # Space complexity: O(n)
    left, right = 0, len(height) - 1
    max_left, max_right = height[left], height[right]
    total_water = 0
    
    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, height[left])
            total_water += max_left - height[left]
        else:
            right -= 1
            max_right = max(max_right, height[right])
            total_water += max_right - height[right]
    
    return total_water

# Alternatively, we can use a two-pointer approach with two passes
def trap_two_pass(height):
    # Time complexity: O(n)
    # Space complexity: O(n)
    left_max = [0] * len(height)
    right_max = [0] * len(height)
    
    for i in range(1, len(height)):
        left_max[i] = max(left_max[i-1], height[i-1])
    
    for i in range(len(height)-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i+1])
    
    total_water = 0
    for i in range(len(height)):
        total_water += max(0, min(left_max[i], right_max[i]) - height[i])
    
    return total_water

# Second alternative is using Stack data structure (preferred when dealing with peaks and valleys)
def trap_stack(height):
    # Time complexity: O(n)
    # Space complexity: O(n)
    stack = []
    total_water = 0
    
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            width = i - stack[-1] - 1
            total_water += width * (min(height[i], height[stack[-1]]) - height[top])
        stack.append(i)
    
    return total_water
