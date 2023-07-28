
class Solution():

    def canConstruct(self, ransomNote, magazine):
        chars = set(magazine)
        for c in ransomNote:
            if c not in chars:
                return False
            chars.remove(c)

        return True


def main():
    ransomNote = "a"
    magzine = "b"
    s = Solution()
    res = s.canConstruct(ransomNote, magzine)
    print(res)

if __name__ == '__main__':
    main()
