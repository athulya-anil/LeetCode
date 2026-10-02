# Last updated: 02/10/2026, 01:08:48
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3
4        for i in range(len(haystack)):
5            j = 0
6
7            for k in range(i, len(haystack)):
8                if haystack[k] == needle[j]:
9                    j += 1
10                else:
11                    break
12
13                if j == len(needle):
14                    return i
15
16        return -1