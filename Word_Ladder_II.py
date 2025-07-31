# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that: Only one letter can be changed at a time Each transformed word must exist in the word list. Note that beginWord is not a transformed word. For example, Given: beginWord = "hit" endWord = "cog" wordList = ["hot","dot","dog","lot","log","cog"] Return [ ["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"] ] Note: Return an empty list if there is no such transformation sequence. All words have the same length. All words contain only lowercase alphabetic characters. You may assume no duplicates in the word list. You may assume beginWord and endWord are non-empty and are not the same. UPDATE (2017/1/20): The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    # Build graph
    word_set = set(wordList)
    if endWord not in word_set:
        return []
    
    graph = defaultdict(list)
    word_set.add(beginWord)
    for word in word_set:
        for i in range(len(word)):
            intermediate_word = word[:i] + '*' + word[i+1:]
            graph[intermediate_word].append(word)
    
    # Find shortest path
    queue = deque([(beginWord, 1, [beginWord])])
    visited = defaultdict(int)
    visited[beginWord] = 1
    result = []
    
    while queue:
        word, level, path = queue.popleft()
        if word == endWord:
            result.append(path)
        for i in range(len(word)):
            intermediate_word = word[:i] + '*' + word[i+1:]
            for neighbor in graph[intermediate_word]:
                if neighbor not in visited or visited[neighbor] == level + 1:
                    queue.append((neighbor, level + 1, path + [neighbor]))
                    visited[neighbor] = level + 1
                elif visited[neighbor] > level + 1:
                    continue
        # Remove explored neighbors
        graph = {k: v for k, v in graph.items() if k not in visited or visited.get(k[0], 0) < level}
    
    # Time complexity: O(N * M^2) where N is the number of words and M is the length of a word
    # Space complexity: O(N * M) as we need to store all intermediate words in the graph
    return result
