# Last updated: 02/05/2026, 15:24:27
1class Solution(object):
2    def solve(self, board):
3        """
4        :type board: List[List[str]]
5        :rtype: None Do not return anything, modify board in-place instead.
6        """
7        u=len(board)
8        v=len(board[0])
9
10        def dfs(i,j):
11            if i<0 or j<0 or i>=u or j>=v or board[i][j] != "O":
12                return
13            else:
14                board[i][j]="T"
15                dfs(i,j-1)
16                dfs(i,j+1)
17                dfs(i-1,j)
18                dfs(i+1,j)       
19
20        for i in range(u):
21            for j in range(v):
22                if i in [0,u-1] or j in [0,v-1]:
23                    dfs(i,j)
24
25        for i in range(u):
26            for j in range(v):
27                if board[i][j]=="O":
28                    board[i][j]="X"
29                elif board[i][j]=="T":
30                    board[i][j]="O"    
31
32                
33        