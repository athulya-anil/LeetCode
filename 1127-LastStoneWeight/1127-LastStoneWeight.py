# Last updated: 14/06/2026, 23:02:39
import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i]=-stones[i]

        heapq.heapify(stones)    

        while len(stones)>1:
            largest=heapq.heappop(stones)    
            second_largest=heapq.heappop(stones)    

            if second_largest != largest:
                heapq.heappush(stones, largest-second_largest)

        if len(stones)==1:
            return(-heapq.heappop(stones))
        else:
            return 0            

            


        