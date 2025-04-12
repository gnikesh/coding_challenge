# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified. You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters. Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. For the last line of text, it should be left justified and no extra space is inserted between words. For example, words: ["This", "is", "an", "example", "of", "text", "justification."] L: 16. Return the formatted lines as: [ "This    is    an", "example  of text", "justification.  " ] Note: Each word is guaranteed not to exceed L in length. click to show corner cases. Corner Cases: A line other than the last line might contain only one word. What should you do in this case? In this case, that line should be left-justified.


def fullJustify(words, maxWidth):
    res, cur, cur_len = [], [], 0
    
    # Time complexity: O(n), where n is the number of words
    for w in words:
        if cur_len + len(w) + len(cur) > maxWidth:
            # Calculate the number of spaces for each interval
            for i in range(maxWidth - cur_len):
                # Distribute extra spaces as evenly as possible
                cur[i % (len(cur) - 1 or 1)] += ' '
            # Join the words in the current line with spaces
            res.append(''.join(cur))
            # Reset the current line
            cur, cur_len = [], 0
        # Add the word to the current line
        cur.append(w)
        cur_len += len(w)

    # Handle the last line
    last_line = ' '.join(cur)
    # Pad the last line with spaces to make its length maxWidth
    last_line += ' ' * (maxWidth - len(last_line))
    res.append(last_line)
    
    return res

# Space complexity: O(n), where n is the total number of characters
