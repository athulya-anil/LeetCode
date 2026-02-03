# Last updated: 03/02/2026, 17:30:41
1class Solution(object):
2    def reverse(self, x):
3        """
4        :type x: int
5        :rtype: int
6        """
7        if x<0:
8            sign=-1
9        else:
10            sign=1
11        x=abs(x)    
12        rev=0
13        while x:
14            d=x%10
15            rev=rev*10+d
16            x=x//10
17        ans=rev*sign
18        if ans < 2**31 - 1 and ans > -2**31:
19            return (ans)
20        else:
21            return 0    
22        
23        