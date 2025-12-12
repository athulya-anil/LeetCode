# Last updated: 12/12/2025, 08:34:15
1class Solution(object):
2    def searchInsert(self, nums, target):
3        beg=0
4        end=len(nums)-1
5        while beg<=end:
6            mid=(beg+end)//2
7            if nums[mid]>=target:
8                end=mid-1
9            else:
10                beg=mid+1
11        return (beg)            
12
13        