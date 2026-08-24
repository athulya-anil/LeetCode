# Last updated: 24/08/2026, 13:30:59
1class Solution(object):
2    def nextGreatestLetter(self, letters, target):
3        """
4        :type letters: List[str]
5        :type target: str
6        :rtype: str
7        """    
8        beg=0
9        end=len(letters)-1
10        
11        if target>=letters[-1]:
12            return(letters[0])
13
14        while beg<end:
15            mid=(beg+end)//2
16            if letters[mid] <= target:
17                beg=mid+1
18            else:
19                end=mid
20        return(letters[end])              
21
22    