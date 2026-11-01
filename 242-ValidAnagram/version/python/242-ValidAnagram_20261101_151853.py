# Last updated: 01/11/2026, 15:18:53
1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        s=sorted(s)
4        t=sorted(t)
5        if s==t:
6            return True
7        else:
8            return False    
9        