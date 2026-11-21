# Last updated: 21/11/2026, 15:25:00
1class Solution:
2    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
3        arr.sort()
4        if len(arr)<=2:
5            return True
6        diffs=arr[1]-arr[0]
7        for i in range(2,len(arr)):
8            if arr[i]-arr[i-1] != diffs:
9                return False
10        return True
11        