# Last updated: 16/11/2026, 22:40:48
1class Solution:
2    def isValidSudoku(self, board: list[list[str]]) -> bool:
3        #check rows
4        set1=set()
5        for i in range(9):
6            set1=set()
7            for j in range(9):
8                if board[i][j] in set1:
9                    return False
10                elif board[i][j] != '.':
11                    set1.add(board[i][j])
12
13        #check cols
14        set1=set()
15        for i in range(9):
16            set1=set()
17            for j in range(9):
18                if board[j][i] in set1:
19                    return False
20                elif board[j][i] != '.':
21                    set1.add(board[j][i])
22        #check box
23        starts=[(0,0),(0,3),(0,6),(3,0),(6,0),(3,3),(3,6),(6,3),(6,6)]
24        
25        for i,j in starts:
26            set1=set()
27            for row in range(i,i+3):
28                for col in range(j,j+3):
29                    if board[row][col] in set1:
30                        return False
31                    elif board[row][col] != '.':
32                        set1.add(board[row][col])
33        return True