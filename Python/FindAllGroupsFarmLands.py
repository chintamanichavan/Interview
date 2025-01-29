class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans=[]
        m,n=len(land),len(land[0])
        for i in range(m):
            for j in range(n):
                if land[i][j]:
                    b=[]
                    b.append(i)
                    b.append(j)
                    q=[(i,j)]
                    while q:
                        ni,nj=q.pop(0)
                        if not land[ni][nj]:continue
                        land[ni][nj]=0
                        li,lj=ni,nj
                        if nj<n-1 and land[ni][nj+1]:q.append((ni,nj+1))
                        if ni<m-1 and land[ni+1][nj]:q.append((ni+1,nj))
                    b.append(ni)
                    b.append(nj)
                    ans.append(b)
        return ans
