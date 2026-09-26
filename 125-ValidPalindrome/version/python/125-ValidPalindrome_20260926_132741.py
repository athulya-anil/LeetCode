# Last updated: 26/09/2026, 13:27:41
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        s = ''.join (c for c in s if c.isalnum())
4        s=s.lower()
5        l=0
6        r=len(s)-1
7        while l<r:
8            if s[l]!=s[r]:
9                return False
10            else:
11                l=l+1
12                r=r-1
13        return True        