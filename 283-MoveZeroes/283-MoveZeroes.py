# Last updated: 03/02/2026, 17:49:39
1class Solution(object):
2    def moveZeroes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7        slow=0
8        fast=0
9
10        while fast<len(nums):
11            if nums[fast]!=0:
12                nums[slow],nums[fast]=nums[fast],nums[slow]
13                slow+=1
14            fast+=1    
15        