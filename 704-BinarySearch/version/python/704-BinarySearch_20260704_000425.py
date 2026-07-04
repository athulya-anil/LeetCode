# Last updated: 04/07/2026, 00:04:25
1class Solution(object):
2    def search(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        beg=0
9        end=len(nums)-1
10        while beg<=end:
11            mid=(beg+end)//2
12            if nums[mid] == target:
13                return(mid)
14            elif nums[mid] > target:
15                end=mid-1
16            else:
17                beg=mid+1
18        return -1                