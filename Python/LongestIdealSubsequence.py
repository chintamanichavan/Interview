class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        l = [0] * 128
        for c in s:
            i = ord(c)
            l[i] = max(l[i - k : i + k + 1]) + 1
        return max(l)
'''
        n=len(s)
        l=[0]*26
        res=0

        for i in range(n):
            y=ord(s[i])-ord('a')
            l[y]+=1
            for j in range(max(y-k,0),min(25,y+k)+1):
                if y!=j:
                    l[y]=max(l[y],1+l[j])
            res=max(res,l[y])

        return res
        '''


