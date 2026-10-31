# Last updated: 31/10/2026, 19:05:14
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total=numBottles
        empties=numBottles
        x=numExchange

        while empties>=x:
            exchange=empties//x
            empties=exchange+(empties%x)
            total+=exchange
        return(total)     