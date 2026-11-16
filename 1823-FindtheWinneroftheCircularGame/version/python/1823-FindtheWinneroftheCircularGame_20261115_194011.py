# Last updated: 15/11/2026, 19:40:11
1from collections import deque
2class Solution:
3    def findTheWinner(self, n: int, k: int) -> int:
4        q=deque(range(1,n+1))
5        while len(q)>1:
6            for _ in range(k-1):
7                q.append(q.popleft())
8            q.popleft()
9        return q.popleft()
10