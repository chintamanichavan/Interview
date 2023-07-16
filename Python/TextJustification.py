class Solution:
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                if len(cur) == 1:
                    res.append( cur[0] + ' ' * (maxWidth - num_of_letters) )
                else:
                    num_spaces = maxWidth - num_of_letters
                    space_between_words, extra_spaces = divmod(num_spaces, len(cur) - 1)
                    for i in range(extra_spaces):
                        cur[i] += ' '
                    res.append((' ' * space_between_words).join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        res.append(' '.join(cur) + ' ' * (maxWidth - num_of_letters - len(cur) + 1))
        return res

def main():
    s = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(s.fullJustify(words, maxWidth))

if __name__ == '__main__':
    main()
