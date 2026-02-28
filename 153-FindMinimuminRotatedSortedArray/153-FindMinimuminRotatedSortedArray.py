# Last updated: 27/02/2026, 20:15:02
1class Solution(object):
2    def findMin(self, nums):
3
4        """
5        :type nums: List[int]
6        :rtype: int
7        """
8        end=len(nums)-1
9        beg=0
10        while beg<end:
11            mid=(beg+end)//2
12            if nums[mid]>nums[end]:
13                beg=mid+1
14            elif nums[mid]<nums[end]:
15                end=mid
16        return(nums[beg])            
17
18
19
20       