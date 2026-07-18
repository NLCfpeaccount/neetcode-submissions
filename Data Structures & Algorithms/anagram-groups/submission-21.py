class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        # Process each string in the input list
        for s in strs:
            # 1. Sort the characters alphabetically: sorted("cat") -> ['a', 'c', 't']
            # 2. Join them back into a single string key: "act"
            sorted_key = "".join(sorted(s))
            
            # Append the original word to the list matching that sorted key
            anagram_map[sorted_key].append(s)
            
        # Return all the values (the nested sublists) from the dictionary
        return list(anagram_map.values())

        