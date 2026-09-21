# Last updated: 21/09/2026, 15:49:55
1class Solution:
2    def connectSticks(self, sticks: list[int]) -> int:
3        total_cost=0
4
5        while len(sticks)>1:
6            sticks.sort()
7            cost=sticks[0]+sticks[1]
8            sticks=sticks[2:]
9            sticks.append(cost)
10            total_cost+=cost
11
12
13        return total_cost    
14
15       