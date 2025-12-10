# Last updated: 10/12/2025, 07:39:44
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
