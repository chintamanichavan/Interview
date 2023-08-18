class Solution:
    def maxProfit(self, prices):
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxProfit = max(maxProfit, prices[i] - prices[i - 1])

        return maxProfit


def main():
    s = Solution()
    prices = [7,1,5,3,6,4]
    res = s.maxProfit(prices)
    print(res)


if __name__ == "__main__":
    main()
