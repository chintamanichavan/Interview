class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        special_count = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    # Check if the current element is the only 1 in its row and column
                    if all(mat[i][k] == 0 for k in range(n) if k != j) and all(mat[k][j] == 0 for k in range(m) if k != i):
                        special_count += 1

        return special_count
