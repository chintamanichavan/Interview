from typing import DefaultDict, List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = DefaultDict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)

    print(res.values())
    return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)