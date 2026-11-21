# Last updated: 21/11/2026, 12:53:46
1from collections import Counter
2class Solution:
3    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
4        a1=Counter(arr1)
5        r=[]
6        for char in arr2:
7            if char in a1:
8                r.extend([char]*a1[char])
9                del a1[char]
10
11        if a1:
12            for i in sorted(a1.keys()):
13                r.extend([i]*a1[i])
14                
15        return (r)   
16
17        