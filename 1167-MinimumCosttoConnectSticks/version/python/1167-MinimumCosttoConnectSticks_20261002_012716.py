# Last updated: 02/10/2026, 01:27:16
1import heapq
2class Solution:
3    def connectSticks(self, sticks: list[int]) -> int:
4        heapq.heapify(sticks)
5        total_cost=0
6        while len(sticks)>1:
7            first_min=heapq.heappop(sticks)
8            second_min=heapq.heappop(sticks)
9            cost=first_min+second_min
10            total_cost+=cost
11            heapq.heappush(sticks,cost)
12
13        return total_cost
14        
15        