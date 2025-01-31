class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        x=[]
        y=[]
        z=""
        for i in s:
            x.append(i)

        for i in x:
            if(i=="1"):
                x.remove(i)
                y.append(i)
                break
        x.sort()
        x.reverse()
        x.extend(y)
        z=z.join(x)
        return(z)
