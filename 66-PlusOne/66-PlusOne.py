# Last updated: 01/01/2026, 21:57:22
1class Solution(object):
2    def plusOne(self, digits):
3        """
4        :type digits: List[int]
5        :rtype: List[int]
6        """
7        n=len(digits)
8
9        for i in range(n-1,-1,-1):
10            if digits[i]<9:
11                digits[i]+=1
12                return(digits)  
13            digits[i]=0
14
15        return [1] + (digits)        
16        