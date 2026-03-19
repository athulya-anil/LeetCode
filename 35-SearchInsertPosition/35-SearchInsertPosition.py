# Last updated: 19/03/2026, 15:12:52
1class Solution(object):
2    def searchInsert(self, nums, target):
3        beg=0
4        end=len(nums)-1
5        while beg<=end:
6            mid=(beg+end)//2
7            if nums[mid]==target:
8                return(mid)
9            elif nums[mid]>target:
10                end=mid-1
11            else:
12                beg=mid+1  
13        return(beg)              
14        