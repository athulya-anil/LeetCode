# Last updated: 18/12/2025, 06:03:22
1class Solution(object):
2    def findPeakElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        beg=0
8        end=len(nums)-1
9        while beg<end:
10            mid=(beg+end)//2
11            if nums[mid]<nums[mid+1]:
12                beg=mid+1
13            else:
14                end=mid
15        return (beg)            