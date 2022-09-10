class Solution:
    
    def bfs(self, grid, x, y, seen):
        
        curr_parameter = 0
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        
        for i in range(4):
            if x+dx[i] < 0 or y+dy[i] < 0 or x+dx[i] >= len(grid) or y+dy[i] >= len(grid[0]) or grid[x+dx[i]][y+dy[i]] == 0:
                
                #print(x, y, x+dx[i], y+dy[i])
                curr_parameter += 1
                continue
            if grid[x+dx[i]][y+dy[i]] == 1 and seen[x+dx[i]][y+dy[i]] == False:
                seen[x+dx[i]][y+dy[i]] = True
                
                seen, parameter = self.bfs(grid, x+dx[i], y+dy[i], seen)
                curr_parameter += parameter
        return seen, curr_parameter
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        parameter = 0
        
        seen = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and seen[i][j] == 0:
                    seen[i][j] = True
                    
                    seen, curr_parameter = self.bfs(grid, i, j, seen)
                    parameter += curr_parameter
        
        return parameter