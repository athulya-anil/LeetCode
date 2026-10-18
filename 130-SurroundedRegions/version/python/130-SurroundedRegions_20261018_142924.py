# Last updated: 18/10/2026, 14:29:24
1class Solution:
2    def solve(self, board: list[list[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        u=len(board)
7        v=len(board[0])
8
9        def dfs(i,j):
10            if i<0 or j<0 or i>=u or j>=v or board[i][j] != "O":
11                return
12            else:
13                board[i][j]="T"
14                dfs(i,j+1)
15                dfs(i,j-1)
16                dfs(i-1,j)
17                dfs(i+1,j)
18            
19        for i in range(u):
20            for j in range(v):
21                if i in [0,u-1] or j in [0,v-1]:
22                    dfs(i,j)
23
24        for i in range(u):
25            for j in range(v):
26                if board[i][j]=="T":
27                    board[i][j]="O"
28                elif board[i][j]=="O":
29                    board[i][j]="X"                 