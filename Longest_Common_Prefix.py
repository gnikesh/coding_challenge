# Write a function to find the longest common prefix string amongst an array of strings.


def longest_common_prefix(strs):
    if not strs: return ""
    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        for string in strs:
            if string[i] != char:
                return shortest_str[:i]
    return shortest_str

# Time Complexity: O(N*M) where N is the number of strings and M is the length of the shortest string
# Space Complexity: O(1) as we are not using any extra space that scales with input size
