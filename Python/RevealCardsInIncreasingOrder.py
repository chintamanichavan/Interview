from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        index = list(range(n))
        result = [0] * n

        for card in sorted(deck):
            result[index.pop(0)] = card
            if index:
                index.append(index.pop(0))

        return result


def main():
    s = Solution()
    print(s.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))  # [2, 13, 3, 11, 5, 17, 7]
    print(s.deckRevealedIncreasing([1, 1000]))                 # [1, 1000]


if __name__ == '__main__':
    main()


# review 2024-11-21
