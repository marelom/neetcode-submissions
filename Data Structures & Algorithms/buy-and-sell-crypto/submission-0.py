class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        bought_price = prices[0]
        profit = None
        sold_price = None
        profit_list = []

        if not prices:
            return 0
            
        for p, v in enumerate(prices):
            if v < bought_price:
                bought_price = v
            profit = v - bought_price
            if profit is not None:
                profit_list.append(profit)   
        max_profit = max(profit_list)

  

        return max_profit or 0           