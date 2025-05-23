class Solution:
    def sortVowels(self, s: str) -> str:
            
        vowels = 'aeiouAEIOU'
        # Extract vowels and sort them
        sorted_vowels = sorted([c for c in s if c in vowels])
        
        # Reconstruct the string, replacing vowels in sorted order
        result = []
        vowel_idx = 0
        for c in s:
            if c in vowels:
                result.append(sorted_vowels[vowel_idx])
                vowel_idx += 1
            else:
                result.append(c)

        return ''.join(result)

