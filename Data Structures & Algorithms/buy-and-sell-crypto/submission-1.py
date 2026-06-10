class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 999
        maxProfit = 0

        for price in prices:
            if price < low:
                low = price 
            
            profit = price - low
            if profit > maxProfit:
                maxProfit = profit 
                
        return maxProfit 