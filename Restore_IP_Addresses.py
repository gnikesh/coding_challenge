# Given a string containing only digits, restore it by returning all possible valid IP address combinations. For example: Given "25525511135", return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


def restore_ip_addresses(s):
    def is_valid(ip):
        """Check if an IP segment is valid"""
        if int(ip) > 255 or (len(ip) > 1 and ip[0] == '0'):
            return False
        return True

    def backtrack(start, path):
        """Generate all possible IP addresses"""
        if len(path) == 4:
            if start == len(s):
                result.append('.'.join(path))
            return
        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]
            if is_valid(segment):
                backtrack(end, path + [segment])

    result = []
    backtrack(0, [])
    return result

# Time complexity: O(3^n) where n is the length of the string
# Space complexity: O(n) for the recursion stack and the result list
