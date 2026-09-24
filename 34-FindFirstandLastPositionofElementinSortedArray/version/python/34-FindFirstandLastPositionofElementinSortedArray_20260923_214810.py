# Last updated: 23/09/2026, 21:48:10
1class Solution:
2    def searchRange(self, nums: list[int], target: int) -> list[int]:
3        def first_pos():
4            beg=0
5            end=len(nums)-1
6            while beg<=end:
7                mid=(beg+end)//2
8                if nums[mid]<target:
9                    beg=mid+1
10                else:
11                    end=mid-1    
12            return(beg)
13        def last_pos():
14            beg=0
15            end=len(nums)-1
16            while beg<=end:
17                mid=(beg+end)//2
18                if nums[mid]<=target:
19                    beg=mid+1
20                else:
21                    end=mid-1    
22            return(end)    
23        first=first_pos()
24        if first == len(nums) or nums[first] != target:
25            return([-1,-1])
26        last=last_pos()    
27        return([first,last]) 