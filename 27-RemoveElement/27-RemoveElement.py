# Last updated: 03/02/2026, 18:11:49
1class Solution(object):
2    def removeElement(self, nums, val):
3        """
4        :type nums: List[int]
5        :type val: int
6        :rtype: int
7        """
8        s=f=0
9        while f<len(nums):
10            if nums[f] != val:
11                nums[f], nums[s] = nums[s], nums[f]
12                s+=1
13            f+=1
14        return(s)        
15
16
17       