# Last updated: 10/07/2026, 11:57:54
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        oldColor=image[sr][sc]
        def dfs(i,j):
            if i<0 or j<0 or i>=len(image) or j>=len(image[0]) or image[i][j] != oldColor or image[i][j] == color:
                return

            image[i][j]=color
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
  
        dfs(sr,sc)    
        return(image)
        

     