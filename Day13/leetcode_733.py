class Solution:
    
    def bfs(self, grid, x, y, seen, color, curr):
        
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        
        for i in range(4):
            if x+dx[i] < 0 or y+dy[i] < 0 or x+dx[i] >= len(grid) or y+dy[i] >= len(grid[0]) or grid[x+dx[i]][y+dy[i]] != curr:
                continue
            if seen[x+dx[i]][y+dy[i]] == False and grid[x+dx[i]][y+dy[i]] == curr:
                seen[x+dx[i]][y+dy[i]] = True
                grid[x+dx[i]][y+dy[i]] = color
                seen, grid = self.bfs(grid, x+dx[i], y+dy[i], seen, color, curr)
        return seen, grid
    
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        seen = [[False for i in range(len(image[0]))] for j in range(len(image))]
        
        seen[sr][sc] = True
        curr = image[sr][sc]
        image[sr][sc] = color
        seen, image = self.bfs(image, sr, sc, seen, color, curr)
        
        return image