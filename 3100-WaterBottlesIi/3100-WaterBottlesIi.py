# Last updated: 31/10/2026, 19:01:55
class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total=numBottles
        empties=numBottles
        x=numExchange
        while empties>=x:
            empties-=x
            total+=1
            empties+=1
            x+=1
        return(total)    
