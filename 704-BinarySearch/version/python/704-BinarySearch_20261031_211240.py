# Last updated: 31/10/2026, 21:12:40
1class Solution:
2    def search(self, nums: list[int], target: int) -> int:
3        beg=0
4        end=len(nums)-1
5
6        while beg<=end:
7            mid=(beg+end)//2
8            if nums[mid]==target:
9                return mid
10            elif nums[mid]<target:
11                beg=mid+1
12            else:
13                end=mid-1
14        return -1                
15        