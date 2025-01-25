class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Initialize a dictionary to count the frequency of each character
        char_count = {}
        for word in words:
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

        # Check if each character's count is divisible by the number of words
        num_words = len(words)
        for count in char_count.values():
            if count % num_words != 0:
                return False

        return True
