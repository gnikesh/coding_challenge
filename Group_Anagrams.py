# Given an array of strings, group anagrams together. For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], Return: [ ["ate", "eat","tea"], ["nat","tan"], ["bat"] ] Note: All inputs will be in lower-case.


def groupAnagrams(strs):
    # Time Complexity: O(n*m*log(m)) 
    # where n is the length of strs and m is the maximum length of a string in strs
    # Space Complexity: O(n*m)
    
    anagrams = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    
    return list(anagrams.values())

# Example usage
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
