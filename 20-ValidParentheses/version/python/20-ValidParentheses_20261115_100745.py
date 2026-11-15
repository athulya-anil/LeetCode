# Last updated: 15/11/2026, 10:07:45
1class Solution:
2    def isValid(self, s: str) -> bool:
3        dict1={")":"(","}":"{","]":"["}
4        stack=[]
5
6        for char in s:
7            if char not in dict1:
8                stack.append(char)
9            else:
10                if stack:
11                    t=stack.pop()
12                    if t != dict1[char]:
13                        return False
14                else:
15                    return False
16        return (True if len(stack) == 0 else False)                   
17        