# Last updated: 16/11/2026, 21:17:56
from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time=0
        q=deque(enumerate(tickets))

        while q:
            i,ticket=q.popleft()
            ticket-=1
            time+=1

            if i==k and ticket==0:
                return time

            if ticket>0:
                q.append((i,ticket))