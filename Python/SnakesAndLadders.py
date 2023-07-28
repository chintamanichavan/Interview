from collections import deque
class Solution():

    def snakesAndLadders(self, board):
        N = len(board)

        def get(s):
            quot, rem = divmod(s - 1, N)
            row = N - 1 - quot
            if row % 2 == N % 2:
                col = rem
            else:
                col = N - 1 - rem
            return row, col

        dist = {1: 0}
        queue = deque([1])
        while queue:
            s = queue.popleft()
            if s == N * N: return dist[s]
            for s2 in range(s + 1, min(s + 6, N * N) + 1):
                r, c = get(s2)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 not in dist:
                    dist[s2] = dist[s] + 1
                    queue.append(s2)
        return -1


def main():
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    s = Solution()
    res = s.snakesAndLadders(board)
    print(res)

if __name__ == '__main__':
    main()
