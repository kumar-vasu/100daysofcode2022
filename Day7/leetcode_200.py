class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        islands = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and seen[i][j] == False:
                    islands += 1
                    seen = self.scout(grid, seen, [i,j])
                    
        return islands
    
    def scout(self, grid, seen, idx):
        i = idx[0]
        j = idx[1]
        seen[i][j] = True
        if i>0 and seen[i-1][j] == False and grid[i-1][j] == "1":
            seen = self.scout(grid, seen, [i-1,j])
        if j>0 and seen[i][j-1] == False and grid[i][j-1] == "1":
            seen = self.scout(grid, seen, [i,j-1])
        if i<len(grid)-1 and seen[i+1][j] == False and grid[i+1][j] == "1": 
            seen = self.scout(grid, seen, [i+1,j])
        if j<len(grid[0])-1 and seen[i][j+1] == False and grid[i][j+1] == "1":
            seen = self.scout(grid, seen, [i,j+1])
        return seen