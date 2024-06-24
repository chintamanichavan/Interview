class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return n-1
        elif n == 3:
            return n-1

        ans = [0,1,1,2]

        for i in range(n-3):
            ans.append(sum(ans[-3:]))
        return ans[-1]


