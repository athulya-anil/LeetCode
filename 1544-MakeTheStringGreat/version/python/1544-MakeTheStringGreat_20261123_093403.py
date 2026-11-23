# Last updated: 23/11/2026, 09:34:03
1class Solution:
2    def makeGood(self, s: str) -> str:
3        seen=[]
4        for char in s:
5            if seen and seen[-1] != char and char.lower() == seen[-1].lower():  
6                seen.pop()
7            else:
8                seen.append(char)    
9
10        return ''.join(c for c in seen)      
11
12        