from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Insert every prefix of every arr1 number into a set, then for each arr2 number
        # strip digits from the right and check membership. Max digit count is ~9.
        prefixes = set()
        for x in arr1:
            while x:
                prefixes.add(x)
                x //= 10

        best = 0
        for y in arr2:
            while y:
                if y in prefixes:
                    best = max(best, len(str(y)))
                    break
                y //= 10
        return best


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix([1, 10, 100], [1000]))  # 3
    print(s.longestCommonPrefix([1, 2, 3], [4, 4, 4]))  # 0
    print(s.longestCommonPrefix([1], [1]))              # 1
