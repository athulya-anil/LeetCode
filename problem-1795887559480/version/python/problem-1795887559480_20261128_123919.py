# Last updated: 28/11/2026, 12:39:19
1class Solution:
2    def commonChars(self, words: list[str]) -> list[str]:
3        word1=Counter(words[0])
4        res=[]
5        for word in words:
6            word2=Counter(word)
7            for char in word1:
8                word1[char]=min(word1[char],word2[char])
9        res=[]
10        for wordx in word1:
11            for i in range(word1[wordx]):
12                    res.append(wordx)
13        return res    
14