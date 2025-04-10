# Given two binary strings, return their sum (also a binary string). For example, a = "11" b = "1" Return "100".


def addBinary(a: str, b: str) -> str:
    # Convert binary strings to integers, add them and then convert back to binary string
    return bin(int(a, 2) + int(b, 2))[2:]
        
# Time complexity: O(max(N, M)) where N and M are the lengths of the binary strings
# Space complexity: O(max(N, M)) for the output string
