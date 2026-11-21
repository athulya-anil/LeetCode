# Last updated: 21/11/2026, 12:01:07
1from functools import cmp_to_key
2class Solution:
3    def largestNumber(self, nums: list[int]) -> str:
4        l=[str(s) for s in nums]    
5
6        def cmp(a,b):
7            if a+b > b+a:
8                return -1
9            elif b+a > a+b:
10                return 1
11            else:
12                return 0    
13
14        s1=sorted(l,key=cmp_to_key(cmp))      
15
16        if max(s1) == '0':
17            return '0'  
18        else:           
19            return ''.join(s for s in s1)
20
21   