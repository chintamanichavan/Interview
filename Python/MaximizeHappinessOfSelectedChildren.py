class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        ans = 0
        neg = 0
        ind = 1
        for i in range(k):
            if happiness[-ind]-neg > 0:
                ans += happiness[-ind]-neg
            neg += 1
            ind += 1
        return ans
