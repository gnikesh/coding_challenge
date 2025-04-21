# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n). For example, S = "ADOBECODEBANC" T = "ABC" Minimum window is "BANC". Note: If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.


from collections import defaultdict

def minWindow(s, t):
    # Space complexity: O(n) for dictionary
    # Time complexity: O(n) for single pass through the string
    if not s or not t:
        return ""

    need, formed = defaultdict(int), defaultdict(int)
    
    for char in t:
        need[char] += 1

    required = len(need)
    l, r = 0, 0

    formed_chars = 0

    min_window = (float('inf'), None, None)

    while r < len(s):
        char = s[r]

        if char in need:
            formed[char] += 1
            if formed[char] == need[char]:
                formed_chars += 1

        while l <= r and formed_chars == required:
            char = s[l]

            if r - l + 1 < min_window[0]:
                min_window = (r - l + 1, l, r)

            if char in need:
                if need[char] <= formed[char] - 1:
                    formed_chars -= 1
                formed[char] -= 1
            l += 1

        r += 1

    return "" if min_window[0] == float('inf') else s[min_window[1]:min_window[2] + 1]
