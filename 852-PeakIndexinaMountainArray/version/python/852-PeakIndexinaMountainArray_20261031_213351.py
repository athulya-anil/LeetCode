# Last updated: 31/10/2026, 21:33:51
1class Solution:
2    def peakIndexInMountainArray(self, arr: list[int]) -> int:
3        beg=0
4        end=len(arr)-1
5
6        while beg<end:
7            mid=(beg+end)//2
8            if arr[mid]<arr[mid+1]:
9                beg=mid+1
10            elif arr[mid]>arr[mid+1]:
11                end=mid
12        return beg        
13        