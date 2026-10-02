# Last updated: 02/10/2026, 01:12:28
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3
4        for i in range(len(haystack)):
5            j=0
6            for k in range(i,len(haystack)):
7                if haystack[k]==needle[j]:
8                    j+=1
9                else:
10                    break  
11                if j == len(needle):          
12                    return i            
13        return -1
14         