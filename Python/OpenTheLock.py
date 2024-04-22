class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target=="0000":
            return 0

        visited=set((int(n[0]),int(n[1]),int(n[2]),int(n[3])) for n in deadends)
        target=(int(target[0]),int(target[1]),int(target[2]),int(target[3]))
        if target in visited:
            return -1
        if (0,0,0,0) in visited:
            return -1

        qu=deque([((0,0,0,0),0)])
        visited.add((0,0,0,0))
        while qu:
            (n1,n2,n3,n4),s=qu.popleft()
            for n in [((n1+1)%10,n2,n3,n4),((n1-1)%10,n2,n3,n4),(n1,(n2+1)%10,n3,n4),(n1,(n2-1)%10,n3,n4),
                      (n1,n2,(n3+1)%10,n4),(n1,n2,(n3-1)%10,n4),(n1,n2,n3,(n4+1)%10),(n1,n2,n3,(n4-1)%10)]:
                if n==target:
                    return s+1
                if n not in visited:
                    visited.add(n)
                    qu.append((n,s+1))
        return -1
