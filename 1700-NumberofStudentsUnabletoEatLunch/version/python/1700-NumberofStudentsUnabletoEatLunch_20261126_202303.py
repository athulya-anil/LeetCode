# Last updated: 26/11/2026, 20:23:03
1from collections import deque
2class Solution:
3    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
4        q=deque(students)
5        stack=sandwiches[::-1]
6        count = 0
7        while q and stack and count<len(q):
8            if q[0] == stack[-1]:
9                stack.pop()
10                q.popleft()
11                count = 0
12            else:
13                q.append(q.popleft())
14                count+=1
15                    
16        return len(q)
17        