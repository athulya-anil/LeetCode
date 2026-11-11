# Last updated: 10/11/2026, 20:33:37
1class Solution:
2    def searchInsert(self, nums: list[int], target: int) -> int:
3        beg=0
4        end=len(nums)-1
5        while beg<=end:
6            mid=(beg+end)//2
7
8            if nums[mid]==target:
9                return mid
10            elif nums[mid]>target:
11                end=mid-1
12            else:
13                beg=mid+1
14        return beg                
15        