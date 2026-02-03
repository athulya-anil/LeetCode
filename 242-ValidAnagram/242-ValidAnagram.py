# Last updated: 03/02/2026, 17:35:33
1from collections import Counter
2class Solution(object):
3    def isAnagram(self, s, t):
4        """
5        :type s: str
6        :type t: str
7        :rtype: bool
8        """
9        s=sorted(s)
10        t=sorted(t)
11        if s==t:
12            return True
13        else:
14            return False    
15        