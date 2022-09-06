class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        islands = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and seen[i][j] == False:
                    island = set()
                    island.add((i,j))
                    seen, island = self.scout(grid, seen, [i,j], island)
                    islands.append(island)
        return islands
    
    def scout(self, grid, seen, idx, islands):
        i = idx[0]
        j = idx[1]
        seen[i][j] = True
        if i>0 and seen[i-1][j] == False and grid[i-1][j] == 1:
            islands.add((i-1,j))
            seen, islands = self.scout(grid, seen, [i-1,j], islands)
        if j>0 and seen[i][j-1] == False and grid[i][j-1] == 1:
            islands.add((i,j-1))
            seen, islands = self.scout(grid, seen, [i,j-1], islands)
        if i<len(grid)-1 and seen[i+1][j] == False and grid[i+1][j] == 1: 
            islands.add((i+1,j))
            seen, islands = self.scout(grid, seen, [i+1,j], islands)
        if j<len(grid[0])-1 and seen[i][j+1] == False and grid[i][j+1] == 1:
            islands.add((i,j+1))
            seen, islands = self.scout(grid, seen, [i,j+1], islands)
        return seen, islands
    
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        islands1 = self.numIslands(grid1)
        islands2 = self.numIslands(grid2)
        count = 0
        for i in islands2:
            for j in islands1:
                if i.issubset(j):
                    count += 1
        return count