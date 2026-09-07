# Last updated: 07/09/2026, 12:53:34
1class Solution(object):
2    def isPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        s=s.lower()
8        s=''.join(c for c in s if c.isalnum())
9        left = 0
10        right=len(s)-1
11        while left<=right:
12            if s[left]!=s[right]:
13                return False              
14            left=left+1
15            right=right-1     
16        return(True)
17
18       