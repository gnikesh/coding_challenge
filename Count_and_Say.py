# The count-and-say sequence is the sequence of integers beginning as follows: 1, 11, 21, 1211, 111221, ... 1 is read off as "one 1" or 11. 11 is read off as "two 1s" or 21. 21 is read off as "one 2, then one 1" or 1211. Given an integer n, generate the nth sequence. Note: The sequence of integers will be represented as a string.


def countAndSay(n: int) -> str:
    # start with the first number in the sequence
    res = '1'
    
    # generate the next n-1 numbers in the sequence
    for _ in range(n - 1):
        # initialize variables to keep track of the current number and its count
        cur_num = res[0]
        cur_count = 1
        temp = ''
        
        # iterate through the current number and generate the next number
        for i in range(1, len(res)):
            if res[i] == cur_num:
                # if the current digit is the same as the previous one, increment the count
                cur_count += 1
            else:
                # if the current digit is different from the previous one, append the count and digit to the result
                temp += str(cur_count) + cur_num
                cur_num = res[i]
                cur_count = 1
        
        # append the count and digit of the last group to the result
        temp += str(cur_count) + cur_num
        res = temp

    return res
# Time Complexity: O(2^n * n) where 2^n is the maximum possible length of the sequence and n is the input number.
# Space Complexity: O(2^n) where 2^n is the maximum possible length of the sequence.
