# Last updated: 23/11/2026, 17:49:58
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack=[]
4        set1={"}":"{","]":"[",")":"("}
5
6        for char in s:
7            if char not in set1:
8                stack.append(char)
9            elif stack:
10                if stack.pop() != set1[char]:
11                    return False
12            else:
13                return False
14
15        return (True if len(stack)==0 else False)               
16                
17        