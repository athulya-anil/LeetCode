# Last updated: 31/10/2026, 21:00:36
1import heapq
2class Solution:
3    def connectSticks(self, sticks: list[int]) -> int:
4        heapq.heapify(sticks)
5        total_cost=0
6        while len(sticks)>1:
7            first_stick=heapq.heappop(sticks)
8            second_stick=heapq.heappop(sticks)
9
10            cost=first_stick+second_stick
11            total_cost+=cost
12            heapq.heappush(sticks,cost)
13            
14        return total_cost    
15
16