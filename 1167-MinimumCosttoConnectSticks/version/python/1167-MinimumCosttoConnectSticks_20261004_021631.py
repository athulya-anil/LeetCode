# Last updated: 04/10/2026, 02:16:31
1import heapq
2class Solution:
3    def connectSticks(self, sticks: list[int]) -> int:
4        heapq.heapify(sticks)
5        total_cost=0
6        while len(sticks)>1:
7
8            min_1 = heapq.heappop(sticks)
9            min_2 = heapq.heappop(sticks)
10            cost_2=min_1+min_2
11            total_cost+=cost_2
12            heapq.heappush(sticks, cost_2)
13
14        return total_cost    
15            
16        
17        