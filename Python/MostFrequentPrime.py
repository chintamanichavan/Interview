class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        def isPrime(num):
            if num <= 10: return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        m, n = len(mat), len(mat[0])
        mx = 0
        dircn = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
        d = defaultdict(int)
        for i in range(m):
            for j in range(n):
                for k in dircn:
                    num = 0
                    ii = i
                    jj = j
                    while ii >= 0 and ii < m and jj < n and jj >= 0:
                        num = num * 10 + mat[ii][jj]
                        
                        if isPrime(num):
                            d[num] += 1
                            mx = max(d[num], mx)
                            
                        ii += k[0]
                        jj += k[1]
                        
        ans = -1
        for i in d:
            if d[i] == mx:
                ans = max(ans, i)
        return ans        
        
