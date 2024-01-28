class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        # Initialize an output image with the same dimensions as img
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                count = 0
                total = 0
                # Check all the surrounding cells including the cell itself
                for x in range(max(i - 1, 0), min(i + 2, m)):
                    for y in range(max(j - 1, 0), min(j + 2, n)):
                        total += img[x][y]
                        count += 1
                # Calculate the floor of the average
                res[i][j] = total // count
        
        return res
