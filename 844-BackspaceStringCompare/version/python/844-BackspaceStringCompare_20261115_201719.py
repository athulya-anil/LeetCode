# Last updated: 15/11/2026, 20:17:19
1class Solution:
2    def backspaceCompare(self, s: str, t: str) -> bool:
3        st1=[]
4        st2=[]
5
6        for char in s:
7            if char != "#":
8                st1.append(char)
9            elif st1:
10                st1.pop()
11
12        for char in t:
13            if char != "#":
14                st2.append(char)
15            elif st2:
16                st2.pop()
17
18        return st1==st2        
19                    