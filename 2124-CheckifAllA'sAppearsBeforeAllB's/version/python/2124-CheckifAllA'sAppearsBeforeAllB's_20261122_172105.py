# Last updated: 22/11/2026, 17:21:05
1class Solution:
2    def checkString(self, s: str) -> bool:
3        b_seen = False
4        for char in s:
5            if b_seen and char == "a":
6                return False                  
7            elif char == "b":
8                b_seen = True
9        return True          
10        