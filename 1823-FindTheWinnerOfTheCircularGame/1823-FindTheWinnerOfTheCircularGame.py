# Last updated: 16/11/2026, 21:18:12
from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q=deque(range(1,n+1))
        while len(q)>1:
            for _ in range(k-1):
                q.append(q.popleft())
            q.popleft()
        return q.popleft()
