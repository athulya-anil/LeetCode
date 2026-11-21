# Last updated: 21/11/2026, 11:17:50
1from collections import Counter
2class Solution:
3    def frequencySort(self, s: str) -> str:
4        freq=Counter(s)
5        l=[]
6        s1=sorted(freq.keys(),key=lambda x: (-freq[x]))
7        for char in s1:
8            l.append(char * freq[char])
9        return "".join(s for s in l)
10        