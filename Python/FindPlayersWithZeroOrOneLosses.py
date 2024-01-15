class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners, losers = set(), set()
        loss_count = {}

        for winner, loser in matches:
            winners.add(winner)
            losers.add(loser)
            loss_count[loser] = loss_count.get(loser, 0) + 1

        # Players with zero losses: in winners but not in losers
        zero_losses = sorted(list(winners - losers))

        # Players with exactly one loss
        one_loss = sorted([player for player, count in loss_count.items() if count == 1])

        return [zero_losses, one_loss]
