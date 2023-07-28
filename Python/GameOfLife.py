class Solution():
    def gameOfLife(self, board):

        rows = len(board)
        cols = len(board[0])

        # Iterate through board
        for r in range(rows):
            for c in range(cols):

                live_neighbors = 0
                # Check 8 neighbors
                for nr in [r - 1, r, r + 1]:
                    for nc in [c - 1, c, c + 1]:
                        if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                            live_neighbors += board[nr][nc] & 1

                # Rules 1, 3
                if board[r][c] and live_neighbors in [2, 3]:
                    board[r][c] ^= 1

                # Rule 4
                if not board[r][c] and live_neighbors == 3:
                    board[r][c] ^= 1
        return board



def main():
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    s = Solution()
    res = s.gameOfLife(board)
    for row in res:
        print(row)

if __name__ == '__main__':
    main()
