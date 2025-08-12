class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        score = 0
        tokens.sort()
        deque = collections.deque(tokens)
        while deque:
            if deque and P >= deque[0]:
                P -= deque.popleft()
                score += 1

            else:
                if len(deque) > 2 and score:
                    P += deque.pop()
                    score -= 1
                else:
                    return score

        return score

# review 2025-08-11
