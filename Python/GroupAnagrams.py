from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        print(res.values())
        return res.values()

def main():
    s = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    s.groupAnagrams(strs)

if __name__ == '__main__':
    main()
