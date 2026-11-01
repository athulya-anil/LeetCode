# Last updated: 01/11/2026, 15:47:59
1class Solution:
2    def isValid(self, s: str) -> bool:
3        dict1={")":"(","}":"{","]":"["}
4        stack=[]
5
6        for char in s:
7            if char in dict1:
8                top_element=stack.pop() if stack else "#"
9                if top_element != dict1[char]:
10                    return False
11            else:        
12                stack.append(char)
13        return not stack
14        