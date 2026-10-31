# Last updated: 31/10/2026, 19:07:46
import heapq
class Solution:
    def connectSticks(self, sticks: list[int]) -> int:
        heapq.heapify(sticks)
        total_cost=0
        while len(sticks)>1:

            min_1 = heapq.heappop(sticks)
            min_2 = heapq.heappop(sticks)
            cost_2=min_1+min_2
            total_cost+=cost_2
            heapq.heappush(sticks, cost_2)

        return total_cost    
            
        
        