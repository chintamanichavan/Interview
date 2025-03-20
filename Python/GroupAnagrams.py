from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        for s in strs:
            # Sort the string to use as a key
            key = tuple(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        
        # Return grouped anagrams
        return list(anagrams.values())
