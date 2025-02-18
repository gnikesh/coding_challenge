# Implement strStr(). Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


def strStr(haystack: str, needle: str) -> int:
    # Time complexity: O((len(haystack) - len(needle) + 1) * len(needle))
    # Space complexity: O(1)
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    return -1

def strStrKMP(haystack: str, needle: str) -> int:
    # Time complexity: O(len(haystack) + len(needle))
    # Space complexity: O(len(needle))
    def compute_prefix(needle):
        prefix = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[j] != needle[i]:
                j = prefix[j - 1]
            if needle[j] == needle[i]:
                j += 1
            prefix[i] = j
        return prefix
    
    if not needle:
        return 0
    prefix = compute_prefix(needle)
    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = prefix[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            return i - j + 1
    return -1
