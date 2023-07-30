class Solution:
    def totalNQueens(self, n: int) -> int:
        def can_place(pos, ocuppied_positions):
            for i in range(ocuppied_positions):
                if pos[i] == pos[ocuppied_positions] or \
                    abs(pos[i] - pos[ocuppied_positions]) == ocuppied_positions - i:
                    return False
            return True

        def place_queens(n, pos, ocuppied_positions):
            if ocuppied_positions == n:
                solutions.append(pos[:])
                return
            for i in range(n):
                pos[ocuppied_positions] = i
                if can_place(pos, ocuppied_positions):
                    place_queens(n, pos, ocuppied_positions + 1)

        solutions = []
        pos = [-1] * n
        place_queens(n, pos, 0)
        return len(solutions)


def main():
    n = 1
    s = Solution()
    res = s.totalNQueens(n)
    print(res)

if __name__ == '__main__':
    main()
