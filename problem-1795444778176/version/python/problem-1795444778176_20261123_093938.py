# Last updated: 23/11/2026, 09:39:38
1class Solution:
2    def removeStars(self, s: str) -> str:
3        stack=[]
4        for char in s:
5            if char != "*":
6                stack.append(char)
7            elif stack and char == "*":
8                stack.pop()
9        return ''.join(c for c in stack)            
10
11        