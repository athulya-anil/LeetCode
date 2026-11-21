# Last updated: 21/11/2026, 15:35:31
1class Solution:
2    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
3        arr.sort()
4        diff=float('inf')
5        l=[]
6        for i in range(1,len(arr)):
7            curr_diff=arr[i]-arr[i-1]
8            diff=min(curr_diff,diff)
9
10        for i in range(1,len(arr)):
11            curr_diff=arr[i]-arr[i-1]  
12            if curr_diff == diff:
13                l.append([arr[i-1],arr[i]])
14        return l