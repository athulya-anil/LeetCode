# Last updated: 19/09/2026, 10:58:01
1class Solution:
2    def connectSticks(self, sticks: list[int]) -> int:
3        total_cost=0
4        while len(sticks)>1:
5            sticks.sort()
6            cost=sticks[0]+sticks[1]
7            sticks=sticks[2:]
8            sticks.append(cost)
9            total_cost+=cost   
10        return(total_cost)