# Last updated: 10/12/2025, 07:42:40
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for i in prices:
            if i<min_price:
                min_price = i
            else:
                max_profit = max(max_profit, i - min_price)    
        return(max_profit)        