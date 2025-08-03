# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that: Only one letter can be changed at a time. Each transformed word must exist in the word list. Note that beginWord is not a transformed word. For example, Given: beginWord = "hit" endWord = "cog" wordList = ["hot","dot","dog","lot","log","cog"] As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5. Note: Return 0 if there is no such transformation sequence. All words have the same length. All words contain only lowercase alphabetic characters. You may assume no duplicates in the word list. You may assume beginWord and endWord are non-empty and are not the same. UPDATE (2017/1/20): The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    # Create a set of words for faster lookup
    word_set = set(wordList)
    
    # Check if endWord is in wordList
    if endWord not in word_set:
        return 0

    # Initialize queue with the starting word
    queue = deque([(beginWord, 1)])  # (word, length)

    while queue:
        word, length = queue.popleft()
        
        # If we've reached the end word, return the length
        if word == endWord:
            return length
        
        # Replace each character in the word with every possible letter
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + char + word[i+1:]
                
                # If the new word is in the word set, add it to the queue and remove it from the word set
                if next_word in word_set:
                    queue.append((next_word, length + 1))
                    word_set.remove(next_word)

    # If we've reached this point, there is no transformation sequence
    return 0

# Time complexity: O(N * M^2) where N is the length of the word list and M is the length of each word
# Space complexity: O(N) for the queue and set
