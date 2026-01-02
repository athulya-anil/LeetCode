# Last updated: 02/01/2026, 22:24:33
1class Solution(object):
2    def repeatedNTimes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        seen=[]
8        repeated=[]
9        length=len(nums)  
10        n=length/2
11        unique_elements=n+1
12        repeated_elements=length-unique_elements
13        for i in nums:
14            if i not in seen:
15                seen.append(i)
16            else:
17                repeated.append(i)    
18                
19        return(repeated[0])        
20
21
22