# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters. For example, given: s: "barfoothefoobarman" words: ["foo", "bar"] You should return the indices: [0,9]. (order does not matter).


from typing import List

def findSubstring(s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []

    word_len = len(words[0])
    total_len = len(words) * word_len
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    result = []
    for i in range(len(s) - total_len + 1):
        seen = {}
        for j in range(len(words)):
            k = i + j * word_len
            word = s[k:k + word_len]
            if word not in word_count:
                break
            seen[word] = seen.get(word, 0) + 1
            if seen[word] > word_count.get(word, 0):
                break
            if j == len(words) - 1:
                result.append(i)

    return result

# Time complexity: O(N*M*logM) where N is the length of string s, and M is the number of words
# Space complexity: O(M) where M is the number of words
