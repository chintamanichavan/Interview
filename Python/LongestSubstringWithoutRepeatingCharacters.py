
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        i = 0
        ans = 0
        n = len(s)
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]],i)

            ans = max(ans, j-i+1)
            mp[s[j]] = j + 1

        print(ans)
        return ans

def main():
    solution = Solution()
    s = "pwwkew"
    solution.lengthOfLongestSubstring(s)

if __name__ == '__main__':
    main()
