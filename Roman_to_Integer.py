# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.


def romanToInt(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    for i in range(len(s)):
        # if the current numeral is smaller than the next one, subtract it
        if i > 0 and roman_map[s[i]] > roman_map[s[i - 1]]:
            result += roman_map[s[i]] - 2 * roman_map[s[i - 1]]
        else:
            result += roman_map[s[i]]
    return result

# Time complexity: O(n)
# Space complexity: O(1)
