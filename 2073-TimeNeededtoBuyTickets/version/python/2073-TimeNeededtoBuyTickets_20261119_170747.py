# Last updated: 19/11/2026, 17:07:47
1from collections import deque
2class Solution:
3    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
4        q=deque(enumerate(tickets))
5        time=0
6        while q:
7            i, t=q.popleft()
8            t=t-1
9            time=time+1
10
11            if t > 0:
12                q.append((i,t))
13                
14            if i == k and t==0:
15                return time
16    
17
18