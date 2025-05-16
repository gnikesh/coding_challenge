# The gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0. For example, given n = 2, return [0,1,3,2]. Its gray code sequence is: 00 - 0 01 - 1 11 - 3 10 - 2 Note: For a given n, a gray code sequence is not uniquely defined. For example, [0,2,3,1] is also a valid gray code sequence according to the above definition. For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.


def grayCode(n):
    # Time complexity: O(2^n) 
    # Space complexity: O(2^n)
    if n == 0:
        return [0]
    res = grayCode(n - 1)
    return res + [x + (1 << (n - 1)) for x in res[::-1]]

def grayCodeIterative(n):
    # Time complexity: O(2^n) 
    # Space complexity: O(2^n)
    res = [0]
    for i in range(n):
        for j in range(len(res) - 1, -1, -1):
            res.append(res[j] + (1 << i))
    return res
