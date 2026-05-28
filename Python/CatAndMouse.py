from collections import deque
from typing import List


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        # Retrograde BFS from terminal states. State = (mouse_pos, cat_pos, turn).
        # Naive minimax loops on cycles; retrograde analysis assigns a definite color
        # (MOUSE/CAT) only when forced, else DRAW.
        # - If a predecessor's player-to-move can reach a state colored as their win, color it that win.
        # - Else decrement the predecessor's degree; when all the player's moves lead to losses, color it the loss.
        MOUSE, CAT, DRAW = 1, 2, 0
        n = len(graph)

        # color[m][c][turn] : 0/1/2 ;   turn in {MOUSE, CAT} = whose turn it is to move
        color = [[[DRAW] * 3 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 3 for _ in range(n)] for _ in range(n)]
        for m in range(n):
            for c in range(n):
                degree[m][c][MOUSE] = len(graph[m])
                degree[m][c][CAT] = len(graph[c]) - (1 if 0 in graph[c] else 0)

        queue: deque = deque()
        for i in range(n):
            for t in (MOUSE, CAT):
                color[0][i][t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i][i][t] = CAT
                    queue.append((i, i, t, CAT))

        while queue:
            m, c, turn, result = queue.popleft()
            # Find predecessors: state from which a single move leads here.
            if turn == MOUSE:
                # Previous turn was CAT; cat moved into c. Predecessor cat positions = graph[c] \ {0}.
                for pc in graph[c]:
                    if pc == 0:
                        continue
                    if color[m][pc][CAT] != DRAW:
                        continue
                    if result == CAT:  # CAT to move at pred and result is CAT-win → pred is CAT-win
                        color[m][pc][CAT] = CAT
                        queue.append((m, pc, CAT, CAT))
                    else:
                        degree[m][pc][CAT] -= 1
                        if degree[m][pc][CAT] == 0:
                            color[m][pc][CAT] = result
                            queue.append((m, pc, CAT, result))
            else:  # turn == CAT
                # Previous turn was MOUSE; mouse moved into m. Predecessor mouse positions = graph[m].
                for pm in graph[m]:
                    if color[pm][c][MOUSE] != DRAW:
                        continue
                    if result == MOUSE:
                        color[pm][c][MOUSE] = MOUSE
                        queue.append((pm, c, MOUSE, MOUSE))
                    else:
                        degree[pm][c][MOUSE] -= 1
                        if degree[pm][c][MOUSE] == 0:
                            color[pm][c][MOUSE] = result
                            queue.append((pm, c, MOUSE, result))

        return color[1][2][MOUSE]


if __name__ == '__main__':
    s = Solution()
    print(s.catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))  # 0
    print(s.catMouseGame([[1, 3], [0], [3], [0, 2]]))                                # 1
