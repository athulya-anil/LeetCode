# Last updated: 27/11/2026, 19:40:52
1class Solution:
2    def minOperations(self, logs: list[str]) -> int:
3        stack=[]
4        ops=0
5        for op in logs:
6            if op == "../":
7                if stack:
8                    stack.pop()
9                else:
10                    continue
11            elif op == "./":
12                continue
13            else:
14                stack.append(op)    
15        while stack:
16            ops+=1
17            stack.pop()        
18        return ops        
19
20
21
22
23        