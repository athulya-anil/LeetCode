# Last updated: 19/09/2026, 13:45:27
1class Solution:
2    def findMin(self, nums: list[int]) -> int:
3        beg=0
4        end=len(nums)-1
5        while beg<end:
6            mid=(beg+end)//2
7            if nums[mid]>nums[end]:
8                beg=mid+1
9            else:
10                end=mid
11        return nums[beg]        
12
13
14        