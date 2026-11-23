# Last updated: 23/11/2026, 17:57:27
1class Solution:
2    def calPoints(self, operations: list[str]) -> int:
3        score=[]
4        for char in operations:
5            if char == "C" and score:
6                score.pop()
7            elif char == "D": 
8                score.append(score[-1]*2)
9            elif char == "+" and score:
10                score.append(score[-1]+score[-2])
11            else:
12                score.append(int(char))   
13
14        if score:
15            return sum(score) 
16        else:
17            return 0          
18        