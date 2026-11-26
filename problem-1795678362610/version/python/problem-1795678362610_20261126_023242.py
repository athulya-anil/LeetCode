# Last updated: 26/11/2026, 02:32:42
1class Solution:
2    def commonChars(self, words: list[str]) -> list[str]:
3
4        first=Counter(words[0])
5        for word in words[1:]:
6            two=Counter(word)
7            for char in first:
8                first[char]=min(first[char],two[char])    
9
10        res=[]
11        for c in first:
12            for i in range(first[c]):
13                res.append(c)
14        return res     
15
16        