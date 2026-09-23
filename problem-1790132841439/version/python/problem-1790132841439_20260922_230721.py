# Last updated: 22/09/2026, 23:07:21
1class Solution:
2    def peakIndexInMountainArray(self, arr: list[int]) -> int:
3        beg=0
4        end=len(arr)-1
5        while beg<end:
6            mid=(beg+end)//2
7
8            if arr[mid]<arr[mid+1]:
9                beg=mid+1
10            else:
11                end=mid   
12                 
13        return (beg)        
14        