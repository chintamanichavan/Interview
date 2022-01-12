def lengthOfLongestSubstring(s: str) -> int:
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


s = "pwwkew"
lengthOfLongestSubstring(s)