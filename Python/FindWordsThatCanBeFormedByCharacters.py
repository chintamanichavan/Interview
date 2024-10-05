class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        

        from collections import Counter

        # Count the characters in chars
        char_count = Counter(chars)

        def is_good(word):
            # Count the characters in the current word
            word_count = Counter(word)
            # Check if each character in word can be formed by characters in chars
            for c in word_count:
                if word_count[c] > char_count[c]:
                    return False
            return True

        # Sum the lengths of all good strings
        return sum(len(word) for word in words if is_good(word))
