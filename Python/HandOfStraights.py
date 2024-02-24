from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        sorted_hand = sorted(hand)

        for card in sorted_hand:
            if count[card] > 0:
                for i in range(groupSize):
                    if count[card + i] > 0:
                        count[card + i] -= 1
                    else:
                        return False
        return True
