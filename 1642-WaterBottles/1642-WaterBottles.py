# Last updated: 14/06/2026, 23:02:06
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