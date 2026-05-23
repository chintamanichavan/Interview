from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        # Greedy: walk seats in pairs. For each pair, if the two people aren't partners,
        # swap whoever is sitting in the right seat with the left person's partner.
        # Partner of p is p ^ 1 (couples are (2k, 2k+1)).
        pos = {p: i for i, p in enumerate(row)}
        swaps = 0
        for i in range(0, len(row), 2):
            partner = row[i] ^ 1
            if row[i + 1] == partner:
                continue
            j = pos[partner]
            row[i + 1], row[j] = row[j], row[i + 1]
            pos[row[j]] = j
            pos[row[i + 1]] = i + 1
            swaps += 1
        return swaps


if __name__ == '__main__':
    s = Solution()
    print(s.minSwapsCouples([0, 2, 1, 3]))           # 1
    print(s.minSwapsCouples([3, 2, 0, 1]))           # 0
    print(s.minSwapsCouples([0, 2, 4, 1, 3, 5]))     # 2
    print(s.minSwapsCouples([5, 4, 2, 6, 3, 1, 0, 7]))  # 2
