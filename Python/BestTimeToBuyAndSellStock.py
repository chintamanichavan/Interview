class Solution:
    def maxProfit(self, prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        print(max_profit)
        return max_profit


def main():
    s = Solution()
    prices = [7,1,5,3,6,4]
    s.maxProfit(prices)


if __name__ == "__main__":
    main()
