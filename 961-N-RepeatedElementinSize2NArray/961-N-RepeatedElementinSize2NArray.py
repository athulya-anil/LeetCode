# Last updated: 02/01/2026, 22:26:16
1class Solution(object):
2    def repeatedNTimes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        seen=[]
8        repeated=[]
9        for i in nums:
10            if i not in seen:
11                seen.append(i)
12            else:
13                repeated.append(i)                
14        return(repeated[0])        
15
16
17