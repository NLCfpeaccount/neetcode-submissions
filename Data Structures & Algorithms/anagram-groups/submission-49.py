from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # A dictionary that automatically creates an empty list for new keys
        anagram_map = defaultdict(list)
        
        for word in strs:
            # 1. Sort the word to create the unique "signature" key
            #    e.g., "cat" -> ['a', 'c', 't'] -> "act"
            sorted_key = "".join(sorted(word))
            
            # 2. Append the original word to this key's list
            anagram_map[sorted_key].append(word)
            
        # 3. Return just the grouped lists
        return list(anagram_map.values())
