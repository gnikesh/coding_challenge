# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively. Below is one possible representation of s1 = "great": great /    \ gr    eat / \    /  \ g   r  e   at / \ a   t To scramble the string, we may choose any non-leaf node and swap its two children. For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat". rgeat /    \ rg    eat / \    /  \ r   g  e   at / \ a   t We say that "rgeat" is a scrambled string of "great". Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae". rgtae /    \ rg    tae / \    /  \ r   g  ta  e / \ t   a We say that "rgtae" is a scrambled string of "great". Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.


def isScrambled(s1: str, s2: str) -> bool:
    # Time complexity: O(3^n * n) where n is the length of s1 and s2
    # Space complexity: O(n) for recursion call stack
    if sorted(s1) != sorted(s2):
        return False
    
    if len(s1) == 1:
        return True
    
    for i in range(1, len(s1)):
        # Check if s2 is a scrambled string of s1 by swapping the substrings at position i
        if (isScrambled(s1[:i], s2[:i]) and isScrambled(s1[i:], s2[i:])) or \
           (isScrambled(s1[:i], s2[-i:]) and isScrambled(s1[i:], s2[:-i])):
            return True
            
    return False

# Example usage:
s1 = "great"
s2 = "rgeat"
print(isScrambled(s1, s2))  # Output: True
