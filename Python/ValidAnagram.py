def isAnagram(s: str, t: str) -> bool:
    s_dict ,t_dict = [0] * 26, [0] * 26
    
    for item in s:
        s_dict[ord(item) - ord('a')] += 1

    for item in t:
        t_dict[ord(item) - ord('a')] += 1

    print(s_dict)
    print(t_dict)
    print(s_dict == t_dict)

    return s_dict == t_dict

s = "anagram"
t = "nagaram"
isAnagram(s,t)