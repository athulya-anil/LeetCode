# Last updated: 26/09/2026, 13:36:26
1class Solution:
2    def connectSticks(self, sticks: list[int]) -> int:
3        
4        total_cost=0
5        while len(sticks)>1:
6            sticks.sort()
7            cost=sticks[0]+sticks[1]
8            sticks=sticks[2:]
9            sticks.append(cost)
10            total_cost+=cost
11        return total_cost    