# Last updated: 03/02/2026, 17:50:36
1class Solution(object):
2    def moveZeroes(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7        f=s=0
8        while f<len(nums):
9            if nums[f]!=0:
10                nums[f],nums[s]=nums[s],nums[f]
11                s+=1
12            f+=1    