class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_tokens = map(int, version1.split("."))
        v2_tokens = map(int, version2.split("."))
        for i, j in zip_longest(v1_tokens, v2_tokens, fillvalue=0):
            if i < j: return -1
            elif i > j: return 1
        return 0
