class Solution:
    
    def bfs(self, grid, x, y, seen):
        
        curr_area = 1
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        
        for i in range(4):
            if x+dx[i] < 0 or y+dy[i] < 0 or x+dx[i] >= len(grid) or y+dy[i] >= len(grid[0]):
                continue
            if grid[x+dx[i]][y+dy[i]] == 1 and seen[x+dx[i]][y+dy[i]] == False:
                seen[x+dx[i]][y+dy[i]] = True
                
                seen, area = self.bfs(grid, x+dx[i], y+dy[i], seen)
                curr_area += area
        return seen, curr_area
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        
        seen = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and seen[i][j] == 0:
                    seen[i][j] = True
                    
                    seen, area = self.bfs(grid, i, j, seen)
                    max_area = max(area, max_area)
        
        return max_area