# Last updated: 25/11/2026, 23:22:59
1class Solution:
2    def canAliceWin(self, n: int) -> bool:
3        count = 10
4        alice = True
5        while n>=count:
6            n -= count
7            count-=1
8            alice = not alice
9        return not alice        
10
11
12
13        