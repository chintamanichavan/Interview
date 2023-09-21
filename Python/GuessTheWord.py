# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        place_counts = collections.defaultdict(int)
        for word in wordlist:
            for i, char in enumerate(word):
                place_counts[str(i)+char] += 1
        
        def word_uniqueness(word):
            score = 0
            for i, char in enumerate(word):
                score += place_counts[str(i)+char]
            return score
        
        # wordlist will be sorted from most to least unique.
        wordlist.sort(key=word_uniqueness)
        
        def word_is_possible(guess_word, word, matches):
            if guess_word == word:
                return False
            match_count = 0
            for a, b in zip(guess_word, word):
                if a == b:
                    match_count += 1
            return match_count == matches
        
        end = -1
        for _ in range(10):
            guess_word = wordlist[end]
            matches = master.guess(guess_word)
            if matches == 6:
                break
            elif matches == 0:
                wordlist = [w for w in wordlist if not any(a==b for a, b in zip(guess_word, w))]
                if end == 0:
                    end = -1
            else:
                wordlist = [w for w in wordlist if word_is_possible(guess_word, w, matches)]
                if end == -1:
                    end = 0
