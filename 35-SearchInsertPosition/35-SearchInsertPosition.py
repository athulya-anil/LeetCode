# Last updated: 17/12/2025, 18:10:51
1class Solution(object):
2    def searchInsert(self, nums, target):
3        beg=0
4        end=len(nums)
5        while beg<end:
6            mid=(beg+end)//2
7            if nums[mid]<target:
8                beg=mid+1
9            else:
10                end=mid
11        return(beg)            
12
13        