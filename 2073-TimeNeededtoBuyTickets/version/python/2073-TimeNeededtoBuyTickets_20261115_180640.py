# Last updated: 15/11/2026, 18:06:40
1from collections import deque
2class Solution:
3    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
4        time=0
5        q=deque(enumerate(tickets))
6
7        while q:
8            i,ticket=q.popleft()
9            ticket-=1
10            time+=1
11
12            if i==k and ticket==0:
13                return time
14
15            if ticket>0:
16                q.append((i,ticket))