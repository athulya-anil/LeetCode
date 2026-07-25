# Last updated: 25/07/2026, 13:01:22
1class Solution(object):
2    def maxProduct(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        dict1=[]
8        max_prod=0
9        for char in str(n):
10            dict1.append(int(char))
11        dict1.sort(reverse=True)    
12        return(dict1[0]*dict1[1])