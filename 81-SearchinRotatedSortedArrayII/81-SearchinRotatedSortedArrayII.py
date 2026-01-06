# Last updated: 06/01/2026, 21:33:28
1class Solution(object):
2    def search(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: bool
7        """
8        beg=0
9        end=len(nums)-1
10        while beg<=end:
11            mid=(beg+end)//2
12            if nums[mid]==target:
13                return (True)
14            if nums[beg] == nums[mid] == nums[end]:
15                beg+=1
16                end-=1   
17                continue
18            if nums[beg]<=nums[mid]: #left is sorted
19                if nums[beg]<=target<nums[mid]:
20                    end=mid-1
21                else:
22                    beg=mid+1
23            else: #right is sorted
24                if nums[mid]<target<=nums[end]:
25                    beg=mid+1
26                else:
27                    end=mid-1  
28        return(False)                          
29