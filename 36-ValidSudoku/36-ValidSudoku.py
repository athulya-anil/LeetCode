# Last updated: 16/11/2026, 21:32:06
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #check cols
        for i in range(9):
            set1=set()
            for j in range(9):
                t=board[i][j]
                if t in set1:
                    return False
                elif t != '.':
                    set1.add(t)
      

        #check rows
        for i in range(9):
            set1=set()
            for j in range(9):
                t=board[j][i]
                if t in set1:
                    return False
                elif t != '.':
                    set1.add(t)
   

        #check box
        starts=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for i, j in starts:
            set1=set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    t=board[row][col]
                    if t in set1:
                        return False
                    elif t!='.':
                        set1.add(t)
        return True                

        