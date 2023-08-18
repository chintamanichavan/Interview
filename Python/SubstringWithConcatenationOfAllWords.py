from collections import Counter, deque

class Solution():

    def findSubstring(self, s, words):
        if not s or not words:
            return []

        wordLen = len(words[0])
        numWords = len(words)
        concatLen = wordLen * numWords

        res = []
        wordsCount = Counter(words)

        for i in range(wordLen):
            left = i
            right = i
            currCount = Counter()

            while right + wordLen <= len(s):
                w = s[right:right+wordLen]
                right += wordLen
                currCount[w] += 1

                while currCount[w] > wordsCount[w]:
                    lw = s[left:left+wordLen]
                    left += wordLen
                    currCount[lw] -= 1

                if right - left == concatLen:
                    res.append(left)

        return res

def main():
    string1 = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    s = Solution()
    result = s.findSubstring(string1, words)
    print(result)

if __name__ == '__main__':
    main()
