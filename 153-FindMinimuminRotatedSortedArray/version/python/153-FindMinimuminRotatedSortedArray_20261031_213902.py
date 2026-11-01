# Last updated: 31/10/2026, 21:39:02
1class Solution:
2    def findMin(self, nums: list[int]) -> int:
3        beg=0
4        end=len(nums)-1
5
6        while beg<end:
7            mid=(beg+end)//2
8            if nums[mid]>nums[end]:
9                beg=mid+1
10            else:
11                end=mid
12
13        return nums[end]            
14        