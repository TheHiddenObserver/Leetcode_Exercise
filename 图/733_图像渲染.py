class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n,m = len(image),len(image[0])
        def dfs(x,y,color,newColor):
            if x<0 or x>= n or y<0 or y>=m or image[x][y] != color or color == newColor:
                return 
            image[x][y] = newColor
            dfs(x+1,y,color,newColor)
            dfs(x-1,y,color,newColor)
            dfs(x,y+1,color,newColor)
            dfs(x,y-1,color,newColor)
        dfs(sr,sc,image[sr][sc],newColor)
        return image
