# Last updated: 12/12/2025, 09:31:43
1class Solution(object):
2    def findMin(self, nums):
3
4        """
5        :type nums: List[int]
6        :rtype: int
7        """
8        beg=0
9        end=len(nums)-1
10        while beg<end:
11            mid=(beg+end)//2
12            if nums[mid]>nums[end]:
13                beg=mid+1
14            else:
15                end=mid
16        return(nums[beg])            
17            
18        