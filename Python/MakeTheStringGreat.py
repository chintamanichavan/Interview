class Solution:
    def makeGood(self, s: str) -> str:
        lst = []
        for letter in s:
            if lst and abs(ord(lst[-1]) - ord(letter)) == 32:
                lst.pop()
            else:
                lst.append(letter)
        return "".join(lst)

