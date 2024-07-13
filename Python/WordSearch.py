class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j, word_index):
            if word_index == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[word_index]:
                return False

            visited[i][j] = True

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if dfs(i + dx, j + dy, word_index + 1):
                    return True

            visited[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
