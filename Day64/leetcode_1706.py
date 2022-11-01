class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])

        @lru_cache(None)
        def falloc(col, row=0):
            if row == rows: return col
            next_col = col + grid[row][col]
            if 0 <= next_col < cols and grid[row][next_col] != -grid[row][col]:
                return falloc(next_col, row+1)
            return -1

        return [falloc(i) for i in range(cols)]