class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        stack = []
        oranges = 0
        rotten = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    stack.append([i,j])
                    oranges += 1
                    rotten += 1
                if grid[i][j] == 1:
                    oranges += 1
        
        moves = -1
        traversed = set()
        
        dx = [0,1,-1,0]
        dy = [1,0,0,-1]
        
        while len(stack) > 0:
                
            moves += 1
            #print(stack)
            curr_len = len(stack)
            
            for _ in range(curr_len):
                curr = stack.pop(0)
                x = curr[0]
                y = curr[1]
                for i in range(4):
                    if x+dx[i] >= 0 and x+dx[i] < len(grid) and y+dy[i] >= 0 and y+dy[i] < len(grid[0]) and (x+dx[i], y+dy[i]) not in traversed and grid[x+dx[i]][y+dy[i]] == 1 and [x+dx[i], y+dy[i]] not in stack:
                        rotten += 1
                        stack.append([x+dx[i], y+dy[i]])
                        
                traversed.add((x, y))
            #print(moves)
            
        if oranges == rotten:
            if oranges <= 1:
                return 0
            return moves
        else:
            return -1
                    
                    
                    
                    
                    
                    