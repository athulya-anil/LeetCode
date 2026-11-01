# Last updated: 31/10/2026, 21:29:23
1class Solution:
2    def findPeakElement(self, nums: list[int]) -> int:
3        beg=0
4        end=len(nums)-1
5        while beg<end:
6            mid=(beg+end)//2
7            if nums[mid]<nums[mid+1]:
8                beg=mid+1
9            else:
10                end=mid
11        return beg            
12
13        