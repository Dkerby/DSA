class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 999
        maxProfit = 0

        # loop through all of the prices once
        for price in prices:
            # track the lowest price so far
            if price < low:
                low = price 
            
            # check if the profit from the lowest price so far
            # minus the current price is larger than the profit
            # we've seen so far
            profit = price - low
            if profit > maxProfit:
                maxProfit = profit 
                
        # return the highest profit value that we found (defaults to 0)
        return maxProfit 