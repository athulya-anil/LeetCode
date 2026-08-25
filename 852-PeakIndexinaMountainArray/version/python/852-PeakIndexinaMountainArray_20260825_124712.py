# Last updated: 25/08/2026, 12:47:12
1class Solution(object):
2    def peakIndexInMountainArray(self, arr):
3        """
4        :type arr: List[int]
5        :rtype: int
6        """
7        beg=0
8        end=len(arr)-1
9        while beg<end:
10            mid=(beg+end)//2
11            if arr[mid]<arr[mid+1]:
12                beg=mid+1
13            else:
14                end=mid
15        return(beg)  
16                 
17        