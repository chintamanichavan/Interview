def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(profit, max_profit)
    print(max_profit)
    return max_profit

prices = [7,1,5,3,6,4]
maxProfit(prices)