# Given numRows, generate the first numRows of Pascal's triangle. For example, given numRows = 5, Return [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]


def generate(numRows):
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Time complexity: O(numRows^2) 
    # Space complexity: O(numRows^2)
    for i in range(1, numRows):
        # Initialize the row with the first element
        row = [1]
        
        # Generate the middle elements of the row
        # by summing adjacent elements from the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # Add the last element to the row
        row.append(1)
        
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle

# Example usage:
numRows = 5
print(generate(numRows))
